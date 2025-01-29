import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merge_df = pd.merge(person, address, how="left", on="personId")
    return merge_df[["firstName", "lastName", "city", "state"]]


testCases = [
    {
        "person": [[1, 'Wang', 'Allen'], [2, 'Alice', 'Bob']],
        "address": [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']],
        "expected": [
            {"firstName": "Wang", "lastName": "Allen", "city": None, "state": None}, 
            {"firstName": "Alice", "lastName": "Bob", "city": "New York City", "state": "New York"}]
    }
]

for i, testcase in enumerate(testCases):
    person = pd.DataFrame(testcase["person"], columns=['personId', 'firstName', 'lastName']).astype({'personId':'Int64', 'firstName':'object', 'lastName':'object'})
    address = pd.DataFrame(testcase["address"], columns=['addressId', 'personId', 'city', 'state']).astype({'addressId':'Int64', 'personId':'Int64', 'city':'object', 'state':'object'})
    output = combine_two_tables(person, address)
    output = output.where(pd.notna(output), None)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")