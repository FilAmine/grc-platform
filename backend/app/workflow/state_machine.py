from dataclasses import dataclass
from typing import Generic, TypeVar

StateT = TypeVar("StateT")


@dataclass(frozen=True)
class Transition(Generic[StateT]):
    name: str
    source: StateT
    target: StateT


class StateMachine(Generic[StateT]):
    def __init__(self, transitions: list[Transition[StateT]]) -> None:
        self._transitions = transitions

    def next_state(self, state: StateT, transition_name: str) -> StateT:
        for transition in self._transitions:
            if transition.source == state and transition.name == transition_name:
                return transition.target
        raise ValueError("Transition is not allowed from the current state")
