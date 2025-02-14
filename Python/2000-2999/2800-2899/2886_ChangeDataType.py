import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype("int")
    return students

testCases = [
    {
        "data": [
            {"student_id": 1, "name": "Ava", "age": 6, "grade": 73.0},
            {"student_id": 2, "name": "Kate", "age": 15, "grade": 87.0}
        ],
        "expected": [
            {"student_id": 1, "name": "Ava", "age": 6, "grade": 73},
            {"student_id": 2, "name": "Kate", "age": 15, "grade": 87}
        ],
    }
]

for i, testcase in enumerate(testCases):
    output = changeDatatype(pd.DataFrame(testcase["data"]))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")