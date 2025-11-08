import cdsapi
import os
import shutil
import traceback
import time

years = ["2020", "2021", "2022", "2023", "2024", "2025"]
months = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12"
]

for year in years:
    year_folder = year
    os.makedirs(year_folder, exist_ok=True)

    for month in months:
        try:
            dataset = "derived-era5-single-levels-daily-statistics"
            request = {
                "product_type": "reanalysis",
                "variable": [
                    "10m_u_component_of_wind",
                    "10m_v_component_of_wind",
                    "2m_dewpoint_temperature",
                    "2m_temperature",
                    "mean_sea_level_pressure",
                    "mean_wave_direction",
                    "mean_wave_period",
                    "sea_surface_temperature",
                    "significant_height_of_combined_wind_waves_and_swell",
                    "surface_pressure",
                    "total_precipitation"
                ],
                "year": year,
                "month": [month],
                "day": [
                    "01", "02", "03",
                    "04", "05", "06",
                    "07", "08", "09",
                    "10", "11", "12",
                    "13", "14", "15",
                    "16", "17", "18",
                    "19", "20", "21",
                    "22", "23", "24",
                    "25", "26", "27",
                    "28", "29", "30",
                    "31"
                ],
                "daily_statistic": "daily_mean",
                "time_zone": "utc+00:00",
                "frequency": "1_hourly"
            }

            client = cdsapi.Client()
            file = client.retrieve(dataset, request).download()

            print(f"File {file} downloaded for month {month}")

            month_folder = os.path.join(year_folder, month)
            os.makedirs(month_folder, exist_ok=True)

            # Get only the filename, not full path
            filename = os.path.basename(file)

            shutil.move(file, os.path.join(month_folder, filename))

            # Add 5-minute sleep between requests
            print(f"Waiting 5 minutes before next request...")
            time.sleep(300)

        except Exception as e:
            print(f"Exception in year {year} and month {month}")
            traceback.print_exc()  # prints full traceback