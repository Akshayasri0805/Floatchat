def get_ai_response(query: str) -> str:
    """
    Provides informative responses about marine science concepts.
    In production, this would call an LLM API.
    """
    q = query.lower()
    
    # Provide context-aware responses for common marine queries
    if "sea surface temperature" in q or "sst" in q:
        return (
            "Sea Surface Temperature (SST) is the temperature of the ocean's surface layer, "
            "typically measured within the top few meters. SST is crucial for understanding "
            "ocean-atmosphere interactions, weather patterns, and marine ecosystems. "
            "Global SST typically ranges from -2°C in polar regions to 30°C in tropical areas. "
            "SST data is collected via satellites, buoys, and ships. "
            "\n\nExample: The NOAA OISST dataset provides daily global SST at 0.25° resolution."
        )
    
    if "ocean" in q or "marine" in q or "sea" in q:
        return (
            f"Marine science question detected: '{query}'\n\n"
            "This system can provide information about ocean data, sea surface temperature, "
            "marine datasets, and oceanographic concepts. "
            "For specific data queries, try asking about SST or temperature measurements."
        )
    
    return (
        f"AI Response for marine query: '{query}'\n\n"
        "This is a simulated AI response. In production, this would connect to "
        "a large language model trained on marine science literature and oceanographic data."
    )
