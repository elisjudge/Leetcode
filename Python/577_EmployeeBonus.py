import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, bonus, how="left", on="empId")
    return merged_df.loc[(merged_df["bonus"] < 1000) | (merged_df["bonus"].isna())][["name", "bonus"]]


testCases = [
    {
        "employee": [[3, 'Brad', None, 4000], [1, 'John', 3, 1000], [2, 'Dan', 3, 2000], [4, 'Thomas', 3, 4000]],
        "bonus": [[2, 500], [4, 2000]],
        "expected": [{"name": "Brad", "bonus": pd.NA}, {"name": "John", "bonus": pd.NA}, {"name": "Dan", "bonus": 500}]
    }
]

for i, testcase in enumerate(testCases):
    employee = pd.DataFrame(testcase["employee"], columns=['empId', 'name', 'supervisor', 'salary']).astype({'empId':'Int64', 'name':'object', 'supervisor':'Int64', 'salary':'Int64'})
    bonus = pd.DataFrame(testcase["bonus"], columns=['empId', 'bonus']).astype({'empId':'Int64', 'bonus':'Int64'})
    output = employee_bonus(employee, bonus)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")