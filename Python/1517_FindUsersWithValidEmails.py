import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Use the correct regex pattern
    valid_emails_df = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$')]
    
    return valid_emails_df



testCases = [
    {
        "users": [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'], [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'], [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'], [7, 'Shapiro', '.shapo@leetcode.com']],
        "expected": [
            {"user_id": 1, "name": "Winston", "mail": "winston@leetcode.com"}, 
            {"user_id": 3, "name": "Annabelle", "mail": "bella-@leetcode.com"}, 
            {"user_id": 4, "name": "Sally", "mail": "sally.come@leetcode.com"}]
    }
]

for i, testcase in enumerate(testCases):
    users = pd.DataFrame(testcase["users"], columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})
    output = valid_emails(users)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")