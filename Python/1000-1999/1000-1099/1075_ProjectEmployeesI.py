import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merge_df = pd.merge(project, employee, on="employee_id")
    result = (
        merge_df.groupby("project_id").agg(
            total_experience = ("experience_years", "sum"),
            employee_count = ("employee_id", "count")
        ).reset_index()
    )
    result["average_years"] = round(result["total_experience"] / result["employee_count"], 2)
    return result[["project_id", "average_years"]]

testCases = [
    {
        "project": [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]],
        "employee": [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 1], [4, 'Doe', 2]],
        "expected": [
            {"project_id": 1, "average_years": 2.00}, 
            {"project_id": 2, "average_years": 2.50}]
    }
]

for i, testcase in enumerate(testCases):
    project = pd.DataFrame(testcase["project"], columns=['project_id', 'employee_id']).astype({'project_id':'Int64', 'employee_id':'Int64'})
    employee = pd.DataFrame(testcase["employee"], columns=['employee_id', 'name', 'experience_years']).astype({'employee_id':'Int64', 'name':'object', 'experience_years':'Int64'})
    output = project_employees_i(project, employee)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")