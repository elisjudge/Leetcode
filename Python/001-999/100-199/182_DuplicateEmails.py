import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person.loc[person["email"].duplicated(keep=False)][["email"]].drop_duplicates().rename(columns={"email": "Email"})

testCases = [
    {
        "person": [[1, 'jacky@yahoo.com'], [2, 'jacky@yahoo.com'], [3, 'jacky@yahoo.com']],
        "expected": [{"Email": 'jacky@yahoo.com'}]
    },
    {
        "person": [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']],
        "expected": [{"Email": 'a@b.com'}]
    },
]

for i, testcase in enumerate(testCases):
    person = pd.DataFrame(testcase["person"], columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})
    output = duplicate_emails(person)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")