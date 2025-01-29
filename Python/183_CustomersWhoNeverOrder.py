import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(customers, orders, how="left", left_on="id", right_on="customerId", suffixes=["_customer", "_order"])
    return merged_df.loc[merged_df["id_order"].isna()][["name"]].rename(columns={"name":"Customers"})

testCases = [
    {
        "customers": [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']],
        "orders": [[1, 3], [2, 1]],
        "expected": [{"Customers": "Henry"}, {"Customers": "Max"}]
    }
]

for i, testcase in enumerate(testCases):
    customers = pd.DataFrame(testcase["customers"], columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
    orders = pd.DataFrame(testcase["orders"], columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})
    output = find_customers(customers, orders)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")