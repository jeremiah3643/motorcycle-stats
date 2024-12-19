import pandas as pd

def create_datasets():
    # Table 11: Motorcycle Crashes by Day of Week
    crashes_by_day = {
        "Day of the Week": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "TOTAL"],
        "2016": [542, 364, 357, 383, 384, 479, 610, 3119],
        "2017": [535, 313, 332, 360, 359, 466, 624, 2989],
        "2018": [426, 257, 350, 331, 333, 472, 533, 2702],
        "2019": [462, 308, 376, 402, 307, 406, 512, 2773],
        "2020": [465, 307, 285, 296, 347, 388, 581, 2669],
        "2021": [483, 299, 326, 393, 351, 452, 571, 2875],
        "AVERAGE": [486, 308, 338, 361, 347, 444, 572, None]
    }
    df_crashes_by_day = pd.DataFrame(crashes_by_day)
    df_crashes_by_day.to_csv("crashes_by_day.csv", index=False)

    # Table 2: Crashes Involving Motorcycle Units by Year
    crashes_by_year = {
        "Year": [2016, 2017, 2018, 2019, 2020, 2021, "TOTAL"],
        "Crashes": [3119, 2989, 2702, 2773, 2669, 2875, 17127],
        "Percent Change": ["8.3%", "-4.2%", "-9.6%", "-2.6%", "-3.8%", "7.7%", "N/A"]
    }
    df_crashes_by_year = pd.DataFrame(crashes_by_year)
    df_crashes_by_year.to_csv("crashes_by_year.csv", index=False)

    # Table 4: Crashes by Crash Type
    crashes_by_type = {
        "Year": [2016, 2017, 2018, 2019, 2020, 2021, "TOTAL"],
        "Fatal Crash": [143, 133, 167, 152, 151, 161, 907],
        "Serious Injury Crash": [688, 643, 604, 636, 666, 686, 3923],
        "Minor Injury Crash": [981, 926, 877, 893, 864, 904, 5445],
        "Possible Injury Crash": [623, 580, 457, 458, 437, 464, 3019],
        "Property Damage Crash": [684, 707, 597, 634, 551, 660, 3883],
        "TOTAL": [3119, 2989, 2702, 2773, 2669, 2875, 17127]
    }
    df_crashes_by_type = pd.DataFrame(crashes_by_type)
    df_crashes_by_type.to_csv("crashes_by_type.csv", index=False)

    # Table 5: Motorcyclist Count by Injury Type
    motorcyclist_injuries = {
        "Year": [2016, 2017, 2018, 2019, 2020, 2021, "TOTAL"],
        "Died Prior": [0, 0, 0, 0, 0, 1, 1],
        "Fatal Injury": [145, 132, 168, 154, 151, 164, 914],
        "Serious Injury": [743, 703, 647, 688, 715, 731, 4227],
        "Minor Injury": [1081, 1027, 987, 983, 959, 998, 6035],
        "Possible Injury": [701, 635, 511, 497, 512, 510, 3367],
        "No Injury": [750, 741, 628, 660, 562, 664, 4005],
        "Unknown": [515, 550, 489, 498, 515, 507, 3074],
        "TOTAL": [3935, 3788, 3430, 3494, 3399, 3577, 21623]
    }
    df_motorcyclist_injuries = pd.DataFrame(motorcyclist_injuries)
    df_motorcyclist_injuries.to_csv("motorcyclist_injuries.csv", index=False)

    # Table 8: Motorcycle Crashes by Month
    crashes_by_month = {
        "Month": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "TOTAL", "AVERAGE"],
        "2016": [65, 102, 225, 323, 348, 388, 393, 340, 392, 349, 172, 76, 3119, 260],
        "2017": [75, 127, 194, 345, 327, 359, 367, 336, 335, 288, 169, 73, 2989, 249],
        "2018": [63, 92, 165, 241, 319, 320, 329, 376, 315, 268, 169, 78, 2702, 225],
        "2019": [52, 84, 179, 281, 297, 324, 353, 347, 409, 252, 189, 98, 2773, 231],
        "2020": [69, 75, 161, 286, 297, 324, 363, 347, 346, 231, 164, 100, 2669, 222],
        "2021": [73, 74, 193, 281, 307, 324, 363, 347, 346, 231, 164, 100, 2875, 240]
    }
    df_crashes_by_month = pd.DataFrame(crashes_by_month)
    df_crashes_by_month.to_csv("crashes_by_month.csv", index=False)

    # Table 20: Motorcycle Crashes by Weather Conditions
    crashes_by_weather = {
        "Weather Conditions": [
            "No Adverse Conditions", "Rain", "Unknown", "Fog", "Other", "Snow", "Severe Crosswinds", "Smog/Smoke", "Blowing Sand/Soil/Dirt", "TOTAL", "AVERAGE", "PERCENT"
        ],
        "2016": [2997, 102, 12, 4, 0, 2, 1, 0, 1, 3119, 2599, 95.1],
        "2017": [2868, 87, 22, 7, 2, 1, 0, 0, 0, 2989, 2491, 94.2],
        "2018": [2566, 118, 9, 7, 2, 1, 1, 2, 0, 2702, 2310, 95.0],
        "2019": [2683, 66, 16, 6, 0, 0, 1, 1, 0, 2773, 2360, 94.7],
        "2020": [2504, 84, 75, 4, 0, 1, 0, 0, 0, 2669, 2201, 95.0],
        "2021": [2678, 112, 71, 10, 1, 1, 0, 0, 0, 2875, 2331, 94.8],
        "TOTAL": [16296, 569, 205, 38, 5, 5, 2, 3, 1, 17127, 13592, 94.9],
        "AVERAGE": [2716, 95, 34, 6, 1, 1, 0, 1, 0, 2855, 2265, 94.8]
    }
    df_crashes_by_weather = pd.DataFrame(crashes_by_weather)
    df_crashes_by_weather.to_csv("crashes_by_weather.csv", index=False)

    print("Datasets created and saved as CSV files.")

if __name__ == "__main__":
    create_datasets()
