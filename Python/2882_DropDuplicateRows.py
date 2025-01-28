import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])

testCases = [
    {
        "data": [
            {"customer_id": 1, "name": "Ella", "email": "emily@example.com"},
            {"customer_id": 2, "name": "David", "email": "michael@example.com"},
            {"customer_id": 3, "name": "Zachary", "email": "sarah@example.com"},
            {"customer_id": 4, "name": "Alice", "email": "john@example.com"},
            {"customer_id": 5, "name": "Finn", "email": "john@example.com"},
            {"customer_id": 6, "name": "Violet", "email": "alice@example.com"},
        ],
        "expected": [
            {"customer_id": 1, "name": "Ella", "email": "emily@example.com"},
            {"customer_id": 2, "name": "David", "email": "michael@example.com"},
            {"customer_id": 3, "name": "Zachary", "email": "sarah@example.com"},
            {"customer_id": 4, "name": "Alice", "email": "john@example.com"},
            {"customer_id": 6, "name": "Violet", "email": "alice@example.com"},
        ],
    }
]

for i, testcase in enumerate(testCases):
    output = dropDuplicateEmails(pd.DataFrame(testcase["data"]))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")