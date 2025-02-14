import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(bonus = employees.salary * 2)

testCases = [
    {
        "data": [
            {"name": "Piper", "salary": 4548},
            {"name": "Grace", "salary": 28150},
            {"name": "Georgia", "salary": 1103},
            {"name": "Willow", "salary": 6593},
            {"name": "Finn", "salary": 74576},
            {"name": "Thomas", "salary": 24433},
        ],
        "expected": [
            {"name": "Piper", "salary": 4548, "bonus": 9096},
            {"name": "Grace", "salary": 28150, "bonus": 56300},
            {"name": "Georgia", "salary": 1103, "bonus": 2206},
            {"name": "Willow", "salary": 6593, "bonus": 13186},
            {"name": "Finn", "salary": 74576, "bonus": 149152},
            {"name": "Thomas", "salary": 24433, "bonus": 48866},
        ],
    }
]

for i, testcase in enumerate(testCases):
    output = createBonusColumn(pd.DataFrame(testcase["data"]))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")