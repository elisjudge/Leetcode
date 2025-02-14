import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    activity.drop_duplicates(inplace=True)
    result = (
        activity.groupby("activity_date")['user_id']
        .nunique()
        .reset_index(name='active_users')
    )
    return result.loc[result["activity_date"].between("2019-06-28", "2019-07-27")].rename(columns={"activity_date":"day"})
    
testCases = [
    {
        "activity": [[1, 1, '2019-07-20', 'open_session'], [1, 1, '2019-07-20', 'scroll_down'], [1, 1, '2019-07-20', 'end_session'], [2, 4, '2019-07-20', 'open_session'], [2, 4, '2019-07-21', 'send_message'], [2, 4, '2019-07-21', 'end_session'], [3, 2, '2019-07-21', 'open_session'], [3, 2, '2019-07-21', 'send_message'], [3, 2, '2019-07-21', 'end_session'], [4, 3, '2019-06-25', 'open_session'], [4, 3, '2019-06-25', 'end_session']],
        "expected": [
            {"day": pd.to_datetime("2019-07-20"), "active_users": 2}, 
            {"day": pd.to_datetime("2019-07-21"), "active_users": 2}]
    }
]

for i, testcase in enumerate(testCases):
    activity = pd.DataFrame(testcase["activity"], columns=['user_id', 'session_id', 'activity_date', 'activity_type']).astype({'user_id':'Int64', 'session_id':'Int64', 'activity_date':'datetime64[ns]', 'activity_type':'object'})
    output = user_activity(activity)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")