import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(visits, transactions, how="left", on="visit_id")
    filter_df = merged_df[merged_df["transaction_id"].isna()]
    result = (
        filter_df.groupby("customer_id")
        .agg(count_no_trans=("visit_id", "count"))
        .reset_index()
    )
    return result

testCases = [
    {
        "visits": [[1, 23], [2, 9], [4, 30], [5, 54], [6, 96], [7, 54], [8, 54]],
        "transactions": [[2, 5, 310], [3, 5, 300], [9, 5, 200], [12, 1, 910], [13, 2, 970]],
        "expected": [
            {"customer_id": 30, "count_no_trans": 1},
            {"customer_id": 54, "count_no_trans": 2},
            {"customer_id": 96, "count_no_trans": 1}]
    }
]

for i, testcase in enumerate(testCases):
    visits = pd.DataFrame(testcase["visits"], columns=['visit_id', 'customer_id']).astype({'visit_id':'Int64', 'customer_id':'Int64'})
    transactions = pd.DataFrame(testcase["transactions"], columns=['transaction_id', 'visit_id', 'amount']).astype({'transaction_id':'Int64', 'visit_id':'Int64', 'amount':'Int64'})
    output = find_customers(visits, transactions)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")