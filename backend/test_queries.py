#!/usr/bin/env python3
"""Quick test script for chat endpoint routing"""
import requests
import json

base_url = "http://127.0.0.1:8000"

test_cases = [
    {
        "name": "Non-marine query",
        "query": "hello world",
        "expected": "non-marine message"
    },
    {
        "name": "Concept query (what is)",
        "query": "What is sea surface temperature?",
        "expected": "AI explanation"
    },
    {
        "name": "Concept query (give sample)",
        "query": "Give a sample value from the mean sea surface temperature dataset",
        "expected": "AI explanation (because of 'give a sample' trigger)"
    },
    {
        "name": "Concept query (explain)",
        "query": "Explain ocean currents",
        "expected": "AI explanation"
    },
    {
        "name": "Dataset query (actual SST fetch)",
        "query": "Get current SST data",
        "expected": "SST dataset value"
    },
    {
        "name": "Dataset query (temperature)",
        "query": "What is the current sea surface temperature?",
        "expected": "SST dataset value"
    },
]

print("Testing FloatChat API endpoints\n" + "="*60)

# Test root endpoint
try:
    r = requests.get(f"{base_url}/")
    print(f"✓ Root endpoint: {r.status_code} - {r.json()}\n")
except Exception as e:
    print(f"✗ Root endpoint failed: {e}\n")

# Test chat endpoint with different queries
for i, test in enumerate(test_cases, 1):
    print(f"\nTest {i}: {test['name']}")
    print(f"Query: \"{test['query']}\"")
    print(f"Expected: {test['expected']}")
    
    try:
        r = requests.post(
            f"{base_url}/chat",
            json={"query": test["query"]},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if r.status_code == 200:
            response_data = r.json()
            print(f"✓ Status: {r.status_code}")
            print(f"Response: {json.dumps(response_data, indent=2)}")
        else:
            print(f"✗ Status: {r.status_code}")
            print(f"Response: {r.text}")
    
    except Exception as e:
        print(f"✗ Request failed: {e}")

print("\n" + "="*60)
print("Testing complete!")
