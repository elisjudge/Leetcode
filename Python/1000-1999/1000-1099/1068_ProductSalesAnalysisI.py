import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(sales, product, how="inner", on="product_id")
    return merged_df[["product_name", "year", "price"]]


testCases = [
    {
        "sales": [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]],
        "product": [[100, 'Nokia'], [200, 'Apple'], [300, 'Samsung']],
        "expected": [
            {"product_name": "Nokia", "year": 2008, "price": 5000},
            {"product_name": "Nokia", "year": 2009, "price": 5000},
            {"product_name": "Apple", "year": 2011, "price": 9000}]
    }
]

for i, testcase in enumerate(testCases):
    sales = pd.DataFrame(testcase["sales"], columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype({'sale_id':'Int64', 'product_id':'Int64', 'year':'Int64', 'quantity':'Int64', 'price':'Int64'})
    product = pd.DataFrame(testcase["product"], columns=['product_id', 'product_name']).astype({'product_id':'Int64', 'product_name':'object'})
    output = sales_analysis(sales, product)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")