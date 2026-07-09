import pytest
from backend.app.workflow.state_machine import IllegalTransitionError, StateMachine, Transition

TRAFFIC_LIGHT = StateMachine(
    [
        Transition("go", "red", "green"),
        Transition("caution", "green", "yellow"),
        Transition("stop", "yellow", "red"),
    ]
)


def test_next_state_follows_named_transition() -> None:
    assert TRAFFIC_LIGHT.next_state("red", "go") == "green"


def test_next_state_rejects_unknown_transition() -> None:
    with pytest.raises(IllegalTransitionError):
        TRAFFIC_LIGHT.next_state("red", "caution")


def test_can_transition_reports_legal_and_illegal_edges() -> None:
    assert TRAFFIC_LIGHT.can_transition("red", "green") is True
    assert TRAFFIC_LIGHT.can_transition("red", "yellow") is False


def test_transition_to_is_idempotent_for_the_same_state() -> None:
    assert TRAFFIC_LIGHT.transition_to("red", "red") == "red"


def test_transition_to_raises_on_illegal_edge() -> None:
    with pytest.raises(IllegalTransitionError):
        TRAFFIC_LIGHT.transition_to("red", "yellow")
