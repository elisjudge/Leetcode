import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees

testCases = [
    {
        "data": [
            {"name": "Jack", "salary": 19666},
            {"name": "Piper", "salary": 74754},
            {"name": "Mia", "salary": 62509},
            {"name": "Ulysses", "salary": 54866},
        ],
        "expected": [
            {"name": "Jack", "salary": 39332},
            {"name": "Piper", "salary": 149508},
            {"name": "Mia", "salary": 125018},
            {"name": "Ulysses", "salary": 109732},
        ],
    }
]

for i, testcase in enumerate(testCases):
    output = modifySalaryColumn(pd.DataFrame(testcase["data"]))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")