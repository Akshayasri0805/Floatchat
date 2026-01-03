import xarray as xr
from typing import Dict, Any


def read_sst_sample(file_path: str) -> Dict[str, float]:
    """
    Reads a NetCDF SST file and returns a small sample value
    from the first time/lat/lon index.
    """
    ds = xr.open_dataset(file_path)
    try:
        sst = ds["sst"]
        value = float(sst.isel(time=0, lat=0, lon=0).values)
        return {"sample_sst_value": value}
    finally:
        ds.close()


def fetch_mean_sst() -> Dict[str, Any]:
    """
    Reads a demo SST NetCDF file and returns the mean SST.
    Adjust the path or logic as needed.
    """
    try:
        ds = xr.open_dataset("backend/data/sst_sample.nc")
    except Exception as e:
        return {"error": f"Failed to open NetCDF file: {e}"}

    try:
        sst = ds["sst"]
        mean_value = float(sst.mean().values)
        return {"mean_sst_value": mean_value}
    except Exception as e:
        return {"error": f"SST variable missing or unreadable: {e}"}
    finally:
        ds.close()
