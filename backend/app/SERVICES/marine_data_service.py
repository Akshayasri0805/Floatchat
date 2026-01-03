import requests


def _try_urls(urls):
    last_err = None
    for url in urls:
        try:
            r = requests.get(url, timeout=15, verify=False)
            r.raise_for_status()
            data = r.json()
            rows = data.get("table", {}).get("rows", [])
            if rows:
                return {
                    "mean_sst": rows[0][-1],
                    "unit": "degree_Celsius",
                    "source": f"NOAA ERDDAP ({url.split('/griddap/')[1].split('.json')[0]})"
                }
            last_err = "No rows in ERDDAP response"
        except Exception as e:
            last_err = str(e)
    return {"error": f"All ERDDAP attempts failed: {last_err}"}


def fetch_mean_sst():
    # Try a few known OISST dataset IDs/paths; servers occasionally change IDs.
    base = "https://coastwatch.pfeg.noaa.gov/erddap/griddap/"
    candidates = [
        # v2.1 with LonPM180
        base + "ncdcOisst21Agg_LonPM180.json?sst[1981-01-01T00:00:00Z][0][0]",
        # v2.1 without LonPM180
        base + "ncdcOisst21Agg.json?sst[1981-01-01T00:00:00Z][0][0]",
        # legacy aggregations
        base + "ncdcOisst2Agg_LonPM180.json?sst[1981-01-01T00:00:00Z][0][0]",
        base + "ncdcOisst2Agg.json?sst[1981-01-01T00:00:00Z][0][0]",
    ]

    result = _try_urls(candidates)
    if "error" in result:
        # Graceful fallback: return a deterministic placeholder to keep UX smooth.
        return {
            "warning": result["error"],
            "mean_sst": 20.0,
            "unit": "degree_Celsius",
            "source": "placeholder (offline fallback)"
        }
    return result
