from dataclasses import dataclass
from typing import Generic, TypeVar

StateT = TypeVar("StateT")


@dataclass(frozen=True)
class Transition(Generic[StateT]):
    name: str
    source: StateT
    target: StateT


class IllegalTransitionError(Exception):
    pass


class StateMachine(Generic[StateT]):
    """A reusable guard for status fields: define the legal (source -> target) edges
    once per domain enum, then every module that has a status field validates
    transitions the same way instead of re-implementing ad hoc checks."""

    def __init__(self, transitions: list[Transition[StateT]]) -> None:
        self._transitions = transitions

    def next_state(self, state: StateT, transition_name: str) -> StateT:
        for transition in self._transitions:
            if transition.source == state and transition.name == transition_name:
                return transition.target
        raise IllegalTransitionError("Transition is not allowed from the current state")

    def can_transition(self, source: StateT, target: StateT) -> bool:
        return any(t.source == source and t.target == target for t in self._transitions)

    def transition_to(self, source: StateT, target: StateT) -> StateT:
        if source == target:
            return target
        if not self.can_transition(source, target):
            raise IllegalTransitionError(f"cannot move from {source!r} to {target!r}")
        return target
