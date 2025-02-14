import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged_df = employees.merge(employee_uni, how="left", on="id")

    merged_df["unique_id"] = (
        merged_df["unique_id"]
        .fillna(-1) 
        .astype("int64")  
        .replace(-1, None) 
    )
    return merged_df[["unique_id", "name"]]


testCases = [
    {
        "employees": [[1, 'Alice'], [7, 'Bob'], [11, 'Meir'], [90, 'Winston'], [3, 'Jonathan']],
        "employeesUni": [[3, 1], [11, 2], [90, 3]],
        "expected": [
            {"unique_id": None, "name": "Alice"}, 
            {"unique_id": None, "name": "Bob"},
            {"unique_id": 2, "name": "Meir"},
            {"unique_id": 3, "name": "Winston"},
            {"unique_id": 1, "name": "Jonathan"}]
    }
]

for i, testcase in enumerate(testCases):
    employees = pd.DataFrame(testcase["employees"], columns=['id', 'name']).astype({'id':'int64', 'name':'object'})
    employee_uni = pd.DataFrame(testcase["employeesUni"], columns=['id', 'unique_id']).astype({'id':'int64', 'unique_id':'int64'})
    output = replace_employee_id(employees, employee_uni)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")