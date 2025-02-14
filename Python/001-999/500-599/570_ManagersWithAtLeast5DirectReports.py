import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    filtered_df = employee.groupby('managerId').size().reset_index(name='report_count').query('report_count >= 5')
    return employee[["name"]].loc[employee['id'].isin(filtered_df["managerId"])]


testCases = [
    {
        "employee": [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]],
        "expected": [{"name": "John"}]
    }
]


for i, testcase in enumerate(testCases):
    employee = pd.DataFrame(testcase["employee"], columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})
    output = find_managers(employee)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")