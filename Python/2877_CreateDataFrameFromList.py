import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])


testCases = [
    {
        "input": [[1,15],[2,11],[3,11],[4,20]],
        "expected": {"headers": ["student_id", "age"], "values": [[1, 15], [2, 11], [3, 11], [4, 20]]}
    }
]

for i, testCase in enumerate(testCases):
    output = createDataframe(testCase["input"])
    headers_match = list(output.columns) == testCase["expected"]["headers"]
    values_match = output.values.tolist() == testCase["expected"]["values"]

    if headers_match and values_match:
        print(f"Test Case {i}: Passed")
    else:
        print(f"Test Case {i}: Failed")
    print(f"Expected headers: {testCase['expected']['headers']}, Output headers: {list(output.columns)}")
    print(f"Expected values: {testCase['expected']['values']}, Output values: {output.values.tolist()}")