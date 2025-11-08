# Source Code Structure

## Modules

### Data (`data/`)

#### `download_era5.py`
Script for downloading [ERA5 post-processed daily statistics on single levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics?tab=overview) data.
- Downloads daily statistics for multiple climate variables
- Organizes data by year and month
- Includes rate limiting to comply with CDS API requirements

**Usage:**
```bash
python src/data/download_era5.py
```

**Note:** Requires CDS API credentials to be configured, see [cdsapi](https://pypi.org/project/cdsapi/).

### Training Pipeline (`train/`)

*To be implemented*

This module will contain:
- Model training scripts
- Training configuration files
- Training utilities and helpers

### Evaluation Pipeline (`eval/`)

*To be implemented*

This module will contain:
- Model evaluation scripts
- Evaluation metrics and analysis tools
- Visualization utilities for results

