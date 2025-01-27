import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer[["name"]].loc[(customer["referee_id"] != 2) | (customer["referee_id"].isna())]

testCases = [
    {
        "data": [[1, 'Will', None], [2, 'Jane', None], [3, 'Alex', 2], [4, 'Bill', None], [5, 'Zack', 1], [6, 'Mark', 2]],
        "expected": [{"name": "Will"}, {"name": "Jane"}, {"name": "Bill"}, {"name": "Zack"}]
    }
]

for i, testcase in enumerate(testCases):
    customer = pd.DataFrame(testcase["data"], columns=['id', 'name', 'referee_id']).astype({'id':'Int64', 'name':'object', 'referee_id':'Int64'})
    output = find_customer_referee(pd.DataFrame(customer))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")