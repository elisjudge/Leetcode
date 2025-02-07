import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher_unique = teacher.drop_duplicates(subset=["teacher_id", "subject_id"])
    result = (
        teacher_unique.groupby("teacher_id").agg(
            cnt=("subject_id", 'count')
        ).reset_index()
    )
    return result

testCases = [
    {
        "teacher": [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]],
        "expected": [{"teacher_id": 1, "cnt": 2}, {"teacher_id": 2, "cnt": 4}]
    }
]

for i, testcase in enumerate(testCases):
    teacher = pd.DataFrame(testcase["teacher"], columns=['teacher_id', 'subject_id', 'dept_id']).astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})
    output = count_unique_subjects(pd.DataFrame(teacher))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")