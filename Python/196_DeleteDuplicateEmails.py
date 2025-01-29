import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by="id", inplace=True)
    person.drop_duplicates(subset="email", keep="first", inplace=True)
    person.reset_index(drop=True, inplace=True)

testCases = [
    {
        "person": [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']],
        "expected": [{"id": 1, "email": "john@example.com"}, {"id": 2, "email": "bob@example.com"}]
    }
]

for i, testcase in enumerate(testCases):
    output = pd.DataFrame(testcase["person"], columns=['id', 'email']).astype({'id':'int64', 'email':'object'})
    delete_duplicate_emails(output)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")