#!/usr/bin/env python3
"""Quick demo of the fixed API"""
import requests
import json

base = "http://127.0.0.1:8000"

print("FloatChat API Test - Fixed Data Fetching")
print("=" * 70)

tests = [
    ("Concept Query (AI Response)", "Give a sample value from the mean sea surface temperature dataset"),
    ("Concept Query 2", "What is sea surface temperature?"),
    ("Dataset Query (Real Data!)", "Get current SST"),
    ("Dataset Query 2", "fetch sea surface temperature"),
]

for title, query in tests:
    print(f"\n{title}")
    print(f"Query: \"{query}\"")
    print("-" * 70)
    
    try:
        r = requests.post(f"{base}/chat", json={"query": query}, timeout=10)
        if r.status_code == 200:
            response_data = r.json()
            print(json.dumps(response_data, indent=2))
        else:
            print(f"Error: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"Failed: {e}")

print("\n" + "=" * 70)
print("✓ Test complete!")
print("\nNote: Concept queries return AI explanations.")
print("      Dataset queries return REAL data from NOAA buoys!")
