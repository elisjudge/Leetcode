import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.loc[animals["weight"] > 100].sort_values(by="weight", ascending=False)[["name"]]

testCases = [
    {
        "data": [
            {"name": "Tatiana", "species": "Snake", "age": 98, "weight": 464},
            {"name": "Khaled", "species": "Giraffe", "age": 50, "weight": 41},
            {"name": "Alex", "species": "Leopard", "age": 6, "weight": 328},
            {"name": "Jonathan", "species": "Monkey", "age": 45, "weight": 463},
            {"name": "Stefan", "species": "Bear", "age": 100, "weight": 50},
            {"name": "Tommy", "species": "Panda", "age": 26, "weight": 349},
        ],
        "expected": [
            {"name": "Tatiana"},
            {"name": "Jonathan"},
            {"name": "Tommy"},
            {"name": "Alex"}
        ],
    }
]

for i, testcase in enumerate(testCases):
    output = findHeavyAnimals(pd.DataFrame(testcase["data"]))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")