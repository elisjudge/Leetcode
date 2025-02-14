import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={"id": "student_id", "first": "first_name", "last": "last_name", "age": "age_in_years"}, inplace=True)
    return students

testCases = [
    {
        "data": [
            {"id": 1, "first": "Mason", "last": "King", "age": 6},
            {"id": 2, "first": "Ava", "last": "Wright", "age": 7},
            {"id": 3, "first": "Taylor", "last": "Hall", "age": 16},
            {"id": 4, "first": "Georgia", "last": "Thompson", "age": 18},
            {"id": 5, "first": "Thomas", "last": "Moore", "age": 10}
        ],
        "expected": [
            {"student_id": 1, "first_name": "Mason", "last_name": "King", "age_in_years": 6},
            {"student_id": 2, "first_name": "Ava", "last_name": "Wright", "age_in_years": 7},
            {"student_id": 3, "first_name": "Taylor", "last_name": "Hall", "age_in_years": 16},
            {"student_id": 4, "first_name": "Georgia", "last_name": "Thompson", "age_in_years": 18},
            {"student_id": 5, "first_name": "Thomas", "last_name": "Moore", "age_in_years": 10}
        ],
    }
]

for i, testcase in enumerate(testCases):
    output = renameColumns(pd.DataFrame(testcase["data"]))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")