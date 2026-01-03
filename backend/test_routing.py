import requests
import json

queries = [
    ("Concept - 'Give sample'", "Give a sample value from the mean sea surface temperature dataset"),
    ("Concept - 'What is'", "What is sea surface temperature?"),
    ("Concept - 'Explain'", "Explain how SST affects weather"),
    ("Dataset - 'Get SST'", "Get current SST"),
    ("Dataset - 'fetch temperature'", "fetch sea surface temperature data"),
    ("Non-marine", "hello world"),
]

print("\nTesting Different Query Types:")
print("=" * 80)

for name, query in queries:
    r = requests.post("http://127.0.0.1:8000/chat", json={"query": query})
    response = r.json()["response"]
    
    # Determine type
    if isinstance(response, dict):
        if "sst_value" in response:
            type_str = "DATASET (Real Data)"
        else:
            type_str = "DATASET (Other)"
    elif "AI Response" in str(response) or "Sea Surface Temperature" in str(response):
        type_str = "CONCEPT (AI)"
    elif "marine" in str(response).lower():
        type_str = "NON-MARINE"
    else:
        type_str = "UNKNOWN"
    
    print(f"\n{name}")
    print(f"Query: {query[:60]}")
    print(f"Type: {type_str}")
    print(f"Response preview: {str(response)[:150]}...")

print("\n" + "=" * 80)
