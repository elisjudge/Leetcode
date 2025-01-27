import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[["tweet_id"]].loc[(tweets["content"].str.len() > 15)]

testCases = [
    {
        "data": [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']],
        "expected": [{"tweet_id": 2}]
    }
]

for i, testcase in enumerate(testCases):
    tweets = pd.DataFrame(testcase["data"], columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})
    output = invalid_tweets(pd.DataFrame(tweets))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")