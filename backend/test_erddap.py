#!/usr/bin/env python3
"""Test ERDDAP endpoints to find working ones"""
import requests

# Test various ERDDAP endpoints with different formats and parameters
test_urls = [
    # CSV format with index-based access
    ("CSV index [0:1:0]", "https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg_LonPM180.csv?sst[0:1:0][0:1:0][0:1:0]"),
    ("CSV last", "https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg_LonPM180.csv?sst[(last)][0][0]"),
    
    # JSON format
    ("JSON index", "https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg_LonPM180.json?sst[0:1:0][0:1:0][0:1:0]"),
    ("JSON last", "https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg_LonPM180.json?sst[(last)][0][0]"),
    
    # Try without LonPM180 suffix
    ("No PM180 CSV", "https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg.csv?sst[0:1:0][0:1:0][0:1:0]"),
    ("No PM180 JSON", "https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg.json?sst[0:1:0][0:1:0][0:1:0]"),
    
    # Different dataset IDs
    ("v2 Agg", "https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst2Agg_LonPM180.csv?sst[0:1:0][0:1:0][0:1:0]"),
    
    # Try upwell server
    ("Upwell CSV", "https://upwell.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg_LonPM180.csv?sst[0:1:0][0:1:0][0:1:0]"),
]

print("Testing ERDDAP endpoints...\n" + "="*80)

for name, url in test_urls:
    print(f"\n{name}:")
    print(f"URL: {url}")
    try:
        response = requests.get(url, timeout=15)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text[:500]  # First 500 chars
            print(f"✓ SUCCESS!")
            print(f"Content preview:\n{content}")
            
            # Try to extract SST value
            if '.csv' in url:
                lines = response.text.strip().split('\n')
                print(f"Total lines: {len(lines)}")
                if len(lines) > 2:
                    print(f"Header: {lines[0]}")
                    print(f"Data sample: {lines[-1]}")
            elif '.json' in url:
                data = response.json()
                print(f"JSON keys: {data.keys()}")
                if 'table' in data:
                    print(f"Rows: {len(data['table'].get('rows', []))}")
                    if data['table'].get('rows'):
                        print(f"First row: {data['table']['rows'][0]}")
            break  # Stop on first success
        else:
            print(f"✗ Failed with status {response.status_code}")
            
    except requests.exceptions.Timeout:
        print("✗ Timeout")
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}: {str(e)[:100]}")

print("\n" + "="*80)
