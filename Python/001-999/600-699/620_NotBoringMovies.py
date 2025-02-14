import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[(cinema["id"] % 2 != 0) & (cinema["description"] != "boring")].sort_values(by="rating", ascending=False) 

testCases = [
    {
        "cinema": [[1, 'War', 'great 3D', 8.9], [2, 'Science', 'fiction', 8.5], [3, 'irish', 'boring', 6.2], [4, 'Ice song', 'Fantacy', 8.6], [5, 'House card', 'Interesting', 9.1]],
        "expected": [{"id": 5, "movie":'House card', "description":'Interesting', "rating": 9.1}, {"id": 1, "movie": 'War', "description": 'great 3D', "rating": 8.9}]
    }
]

for i, testcase in enumerate(testCases):
    cinema = pd.DataFrame(testcase["cinema"], columns=['id', 'movie', 'description', 'rating']).astype({'id':'Int64', 'movie':'object', 'description':'object', 'rating':'Float64'})
    output = not_boring_movies(cinema)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")