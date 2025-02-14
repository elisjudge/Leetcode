import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars=["product"], 
        value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4",],
        var_name="quarter",
        value_name="sales")


testCases = [
    {
        "data": [
            {"product": "Umbrella", "quarter_1": 417, "quarter_2": 224, "quarter_3": 379, "quarter_4": 611},
            {"product": "SleepingBag", "quarter_1": 800, "quarter_2": 936, "quarter_3": 93, "quarter_4": 875},
        ],
        "expected": [
            {"product": "Umbrella", "quarter": "quarter_1", "sales": 417},
            {"product": "SleepingBag", "quarter": "quarter_1", "sales": 800},
            {"product": "Umbrella", "quarter": "quarter_2", "sales": 224},
            {"product": "SleepingBag", "quarter": "quarter_2", "sales": 936},
            {"product": "Umbrella", "quarter": "quarter_3", "sales": 379},
            {"product": "SleepingBag", "quarter": "quarter_3", "sales": 93},
            {"product": "Umbrella", "quarter": "quarter_4", "sales": 611},
            {"product": "SleepingBag", "quarter": "quarter_4", "sales": 875}
        ],
    }
]

for i, testcase in enumerate(testCases):
    output = meltTable(pd.DataFrame(testcase["data"]))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")