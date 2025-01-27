import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[["product_id"]].loc[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")]


testCases = [
    {
        "data": [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']],
        "expected": [{"product_id": 1}, {"product_id": 3}]
    }
]

for i, testcase in enumerate(testCases):
    products = pd.DataFrame(testcase["data"], columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})
    output = find_products(pd.DataFrame(products))
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")