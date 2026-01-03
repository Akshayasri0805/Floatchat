def resolve_dataset(query: str) -> dict:
    """
    Lightweight resolver that classifies a marine query into either:
    - concept: general questions answered by the AI service
    - dataset selections (e.g., 'sst') handled by data services
    - not_supported: when we don't recognize a dataset yet
    """
    q = query.lower()

    # Concept-style questions
    concept_triggers = [
        "what is", "explain", "define", "meaning of", "how does"
    ]
    if any(t in q for t in concept_triggers):
        return {"type": "concept"}

    # Dataset mapping (expand as needed)
    sst_triggers = ["sst", "sea surface temperature", "surface temperature"]
    if any(t in q for t in sst_triggers):
        return {"dataset": "sst"}

    return {
        "status": "not_supported",
        "message": "Requested dataset or query type is not supported yet."
    }
