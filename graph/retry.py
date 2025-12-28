from graph.state import GraphState


def should_retry(state: GraphState) -> str:
    """
    Decides whether the system should retry or stop.
    """
    if state.retry_count < state.max_retries:
        state.retry_count += 1
        return "retry"
    return "fail"

