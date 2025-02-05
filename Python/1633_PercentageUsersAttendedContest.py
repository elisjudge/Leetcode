import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(register, users, on="user_id")
    result = (
        merged_df.groupby("contest_id").agg(
            n_registered_users = ("user_id", "count")
        ).reset_index()
    )    
    result["n_users"] = len(users)

    result["percentage"] = round(result["n_registered_users"] * 100.0 / result["n_users"], 2)
    result.sort_values(by=["percentage", "contest_id"], ascending=[False, True], inplace=True)

    return result[["contest_id", "percentage"]]

testCases = [
    {
        "users": [[6, 'Alice'], [2, 'Bob'], [7, 'Alex']],
        "register": [[215, 6], [209, 2], [208, 2], [210, 6], [208, 6], [209, 7], [209, 6], [215, 7], [208, 7], [210, 2], [207, 2], [210, 7]],
        "expected": [
            {"contest_id": 208, "percentage": 100.0}, 
            {"contest_id": 209, "percentage": 100.0}, 
            {"contest_id": 210, "percentage": 100.0}, 
            {"contest_id": 215, "percentage": 66.67}, 
            {"contest_id": 207, "percentage": 33.33}]
    }
]

for i, testcase in enumerate(testCases):
    users = pd.DataFrame(testcase["users"], columns=['user_id', 'user_name']).astype({'user_id':'Int64', 'user_name':'object'})
    register = pd.DataFrame(testcase["register"], columns=['contest_id', 'user_id']).astype({'contest_id':'Int64', 'user_id':'Int64'})
    output = users_percentage(users, register)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")