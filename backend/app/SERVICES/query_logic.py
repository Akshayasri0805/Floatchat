def analyze_query(query: str) -> dict:
    query_lower = query.lower()

    marine_keywords = [
        "sea",
        "ocean",
        "marine",
        "sst",
        "temperature"
    ]

    is_marine = any(word in query_lower for word in marine_keywords)

    if not is_marine:
        return {
            "type": "non-marine",
            "message": "This system only supports marine-related questions."
        }

    return {
        "type": "marine"
    }
