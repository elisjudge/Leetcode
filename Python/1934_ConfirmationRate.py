import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    merge_df = pd.merge(signups, confirmations, how="left", on="user_id", suffixes=["_sign", "_confirm"])
    aggregated = merge_df.groupby(["user_id"]).agg(
        confirmed_count = ('action', lambda x: (x == 'confirmed').sum()),
        total_count=('action', 'count')
    ).reset_index()
    aggregated["confirmation_rate"] = aggregated.apply(
        lambda row: round(row['confirmed_count'] / row['total_count'], 2) if row['total_count'] > 0 else 0.00,
        axis = 1
    )
    return aggregated[['user_id', 'confirmation_rate']]

testCases = [
    {
        "signups": [[3, '2020-03-21 10:16:13'], [7, '2020-01-04 13:57:59'], [2, '2020-07-29 23:09:44'], [6, '2020-12-09 10:39:37']],
        "confirmations": [[3, '2021-01-06 03:30:46', 'timeout'], [3, '2021-07-14 14:00:00', 'timeout'], [7, '2021-06-12 11:57:29', 'confirmed'], [7, '2021-06-13 12:58:28', 'confirmed'], [7, '2021-06-14 13:59:27', 'confirmed'], [2, '2021-01-22 00:00:00', 'confirmed'], [2, '2021-02-28 23:59:59', 'timeout']],
        "expected": [
            {"user_id": 2, "confirmation_rate": 0.50},
            {"user_id": 3, "confirmation_rate": 0.00},
            {"user_id": 6, "confirmation_rate": 0.00}, 
            {"user_id": 7, "confirmation_rate": 1.00}]
    }
]

for i, testcase in enumerate(testCases):
    signups = pd.DataFrame(testcase["signups"], columns=['user_id', 'time_stamp']).astype({'user_id':'Int64', 'time_stamp':'datetime64[ns]'})
    confirmations = pd.DataFrame(testcase["confirmations"], columns=['user_id', 'time_stamp', 'action']).astype({'user_id':'Int64', 'time_stamp':'datetime64[ns]', 'action':'object'})
    output = confirmation_rate(signups, confirmations)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")