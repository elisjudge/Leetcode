import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["name"].notna()]

testCases = [
    {
        "data": [
            {"student_id": 32, "name": "Piper", "age": 5},
            {"student_id": 217, "name": None, "age": 19},
            {"student_id": 779, "name": "Georgia", "age": 20},
            {"student_id": 849, "name": "Willow", "age": 14}
        ],
        "expected": [
            {"student_id": 32, "name": "Piper", "age": 5},
            {"student_id": 779, "name": "Georgia", "age": 20},
            {"student_id": 849, "name": "Willow", "age": 14}
        ],
    }
]

for i, testcase in enumerate(testCases):
    output = dropMissingData(pd.DataFrame(testcase["data"]))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")