import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merge_df = pd.merge(orders, products, how="left", on="product_id")
    february_orders = merge_df[
        (merge_df['order_date'] >= '2020-02-01') & (merge_df['order_date'] <= '2020-02-29')
    ]

    result = (
        february_orders.groupby('product_name')['unit']
        .sum()
        .reset_index()
    )
    return result.loc[result["unit"] >= 100]    


testCases = [
    {
        "products": [[1, 'Leetcode Solutions', 'Book'], [2, 'Jewels of Stringology', 'Book'], [3, 'HP', 'Laptop'], [4, 'Lenovo', 'Laptop'], [5, 'Leetcode Kit', 'T-shirt']],
        "orders": [[1, '2020-02-05', 60], [1, '2020-02-10', 70], [2, '2020-01-18', 30], [2, '2020-02-11', 80], [3, '2020-02-17', 2], [3, '2020-02-24', 3], [4, '2020-03-01', 20], [4, '2020-03-04', 30], [4, '2020-03-04', 60], [5, '2020-02-25', 50], [5, '2020-02-27', 50], [5, '2020-03-01', 50]],
        "expected": [
            {"product_name": "Leetcode Kit", "unit": 100},
            {"product_name": "Leetcode Solutions", "unit": 130}]
    }
]

for i, testcase in enumerate(testCases):
    products = pd.DataFrame(testcase["products"], columns=['product_id', 'product_name', 'product_category']).astype({'product_id':'Int64', 'product_name':'object', 'product_category':'object'})
    orders = pd.DataFrame(testcase["orders"], columns=['product_id', 'order_date', 'unit']).astype({'product_id':'Int64', 'order_date':'datetime64[ns]', 'unit':'Int64'})
    output = list_products(products, orders)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")