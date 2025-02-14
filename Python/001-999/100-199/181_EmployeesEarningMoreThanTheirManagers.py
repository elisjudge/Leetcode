import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    selfjoin = employee.merge(employee, left_on='managerId', right_on='id', suffixes=('', '_manager'))
    return selfjoin.loc[(selfjoin["salary"] > selfjoin["salary_manager"])][["name"]].rename(columns={"name":"Employee"})


testCases = [
    {
        "employee": [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]],
        "expected": [{"Employee": "Joe"}]
    }
]

for i, testcase in enumerate(testCases):
    employee = pd.DataFrame(testcase["employee"], columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})
    output = find_employees(employee)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")