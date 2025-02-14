import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]

testCases = [
    {
        "data": {
            "student_id": [101, 53, 128, 3],
            "name": ["Ulysses", "William", "Henry", "Henry"],
            "age": [13, 10, 6, 11]
        },
        "expected": [{"name": "Ulysses", "age": 13}]
    }
]

for i, testcase in enumerate(testCases):
    output = selectData(pd.DataFrame(testcase["data"]))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")