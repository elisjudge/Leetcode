import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index="month", columns="city", values="temperature")


testCases = [
    {
        "data": [
            {"city": "Jacksonville", "month": "January", "temperature": 13},
            {"city": "Jacksonville", "month": "February", "temperature": 23},
            {"city": "Jacksonville", "month": "March", "temperature": 38},
            {"city": "Jacksonville", "month": "April", "temperature": 5},
            {"city": "Jacksonville", "month": "May", "temperature": 34},
            {"city": "ElPaso", "month": "January", "temperature": 20},
            {"city": "ElPaso", "month": "February", "temperature": 6},
            {"city": "ElPaso", "month": "March", "temperature": 26},
            {"city": "ElPaso", "month": "April", "temperature": 2},
            {"city": "ElPaso", "month": "May", "temperature": 43},
        ],
        "expected": [
            {"ElPaso": 2, "Jacksonville": 5}, # April
            {"ElPaso": 6, "Jacksonville": 23}, # February
            {"ElPaso": 20, "Jacksonville": 13}, # January
            {"ElPaso": 26, "Jacksonville": 38}, # March
            {"ElPaso": 43, "Jacksonville": 34}, # May
        ],
    }
]

for i, testcase in enumerate(testCases):
    output = pivotTable(pd.DataFrame(testcase["data"]))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")