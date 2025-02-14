import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        pd.unique(
            views["author_id"].loc[
                (views["author_id"] == views["viewer_id"])]),
        columns=["id"]).sort_values("id", ascending=True)

testCases = [
    {
        "data": [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']],
        "expected": [{"id": 4}, {"id": 7}]
    }
]

for i, testcase in enumerate(testCases):
    views = pd.DataFrame(testcase["data"], columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})
    output = article_views(pd.DataFrame(views))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")