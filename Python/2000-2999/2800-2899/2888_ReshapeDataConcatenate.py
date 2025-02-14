import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)

testCases = [
    {
        "df1": [
            {"student_id": 1, "name": "Mason", "age": 8},
            {"student_id": 2, "name": "Ava", "age": 6},
            {"student_id": 3, "name": "Taylor", "age": 15},
            {"student_id": 4, "name": "Georgia", "age": 17}],
        "df2": [
            {"student_id": 5, "name": "Leo", "age": 7},
            {"student_id": 6, "name": "Alex", "age": 7}],
        "expected": [
            {"student_id": 1, "name": "Mason", "age": 8},
            {"student_id": 2, "name": "Ava", "age": 6},
            {"student_id": 3, "name": "Taylor", "age": 15},
            {"student_id": 4, "name": "Georgia", "age": 17},
            {"student_id": 5, "name": "Leo", "age": 7},
            {"student_id": 6, "name": "Alex", "age": 7}],
    }
]

for i, testcase in enumerate(testCases):
    df1 = pd.DataFrame(testcase["df1"])
    df2 = pd.DataFrame(testcase["df2"])
    output = concatenateTables(df1, df2)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")