import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    return products.fillna({'quantity':0})



testCases = [
    {
        "data": [
            {"name": "Wristwatch", "quantity": None, "price": 135},
            {"name": "WirelessEarbuds", "quantity": None, "price": 821},
            {"name": "GolfClubs", "quantity": 779, "price": 9319},
            {"name": "Printer", "quantity": 849, "price": 3501}
        ],
        "expected": [
            {"name": "Wristwatch", "quantity": 0, "price": 135},
            {"name": "WirelessEarbuds", "quantity": 0, "price": 821},
            {"name": "GolfClubs", "quantity": 779, "price": 9319},
            {"name": "Printer", "quantity": 849, "price": 3501}
        ],
    }
]

for i, testcase in enumerate(testCases):
    output = fillMissingValues(pd.DataFrame(testcase["data"]))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")