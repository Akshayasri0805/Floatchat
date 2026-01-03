import requests
from datetime import datetime, timedelta


def fetch_mean_sst():
    """
    Fetches SST data from various marine data APIs.
    Tries multiple sources in order of preference.
    """
    
    # Method 1: Try NOAA CO-OPS (Center for Operational Oceanographic Products and Services)
    # This is a reliable API for nearshore data
    try:
        # Get data from a buoy station (example: Station 8410140 Eastport, ME)
        # This API is more reliable than ERDDAP for simple queries
        station_id = "8410140"  # Eastport, Maine - reliable station
        end_date = datetime.now()
        begin_date = end_date - timedelta(days=1)
        
        url = (
            f"https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?"
            f"begin_date={begin_date.strftime('%Y%m%d')}&"
            f"end_date={end_date.strftime('%Y%m%d')}&"
            f"station={station_id}&"
            f"product=water_temperature&"
            f"units=metric&"
            f"time_zone=gmt&"
            f"application=FloatChat&"
            f"format=json"
        )
        
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and len(data['data']) > 0:
                # Get the most recent reading
                latest = data['data'][-1]
                temp_value = float(latest['v'])
                return {
                    "sst_value": temp_value,
                    "unit": "degree_Celsius",
                    "source": "NOAA CO-OPS Buoy Station",
                    "station": f"Station {station_id} (Eastport, ME)",
                    "timestamp": latest['t'],
                    "note": "Real-time water temperature from NOAA buoy"
                }
    except Exception as e:
        pass  # Try next method
    
    # Method 2: Use Open-Meteo Marine API (free, no auth required)
    try:
        # Get SST for a sample location (tropical Pacific)
        url = (
            "https://marine-api.open-meteo.com/v1/marine?"
            "latitude=0&longitude=-140&"
            "current=ocean_surface_temperature"
        )
        
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if 'current' in data and 'ocean_surface_temperature' in data['current']:
                temp_value = data['current']['ocean_surface_temperature']
                if temp_value is not None:
                    return {
                        "sst_value": temp_value,
                        "unit": "degree_Celsius",
                        "source": "Open-Meteo Marine API",
                        "location": "Tropical Pacific (0°N, 140°W)",
                        "timestamp": data['current'].get('time', 'recent'),
                        "note": "Current ocean surface temperature from marine forecast model"
                    }
    except Exception as e:
        pass  # Try next method
    
    # Fallback: Return realistic simulated data with educational value
    import random
    # Simulate realistic SST based on time of year (Northern Hemisphere)
    month = datetime.now().month
    # Warmer in summer (Jun-Aug), cooler in winter (Dec-Feb)
    base_temp = 15.0
    seasonal_variation = 8.0 * (0.5 - abs(month - 7) / 12.0)
    simulated_temp = round(base_temp + seasonal_variation + random.uniform(-1, 1), 1)
    
    return {
        "sst_value": simulated_temp,
        "unit": "degree_Celsius",
        "source": "Simulated (External APIs unavailable)",
        "location": "Mid-latitude ocean (simulated)",
        "note": f"This is simulated data for demonstration. Real SST APIs are temporarily unavailable. Simulated seasonal variation for month {month}. Typical ocean SST ranges from -2°C (polar) to 30°C (tropical).",
        "fallback": True
    }
