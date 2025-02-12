import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[["name", "population", "area"]].loc[(world["area"] >= 3000000) | (world["population"] >= 25000000)]

testCases = [
    {
        "data": [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000], ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000], ['Angola', 'Africa', 1246700, 20609294, 100990000000]],
        "expected": [{"name": "Afghanistan", "population": 25500100, "area": 652230}, {"name": "Algeria", "population": 37100000, "area": 2381741}]
    }
]

for i, testcase in enumerate(testCases):
    world = pd.DataFrame(testcase["data"], columns=['name', 'continent', 'area', 'population', 'gdp']).astype({'name':'object', 'continent':'object', 'area':'Int64', 'population':'Int64', 'gdp':'Int64'})
    output = big_countries(pd.DataFrame(world))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")
