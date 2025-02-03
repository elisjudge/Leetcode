import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(prices, units_sold, how="left", on="product_id")
    merged_df = merged_df[
        (merged_df['purchase_date'].isna()) |
        ((merged_df['purchase_date'] >= merged_df['start_date']) & 
        (merged_df['purchase_date'] <= merged_df['end_date']))]
    
    merged_df['units'] = merged_df['units'].fillna(0)
    merged_df['sale_price'] = merged_df['units'] * merged_df['price']

    result = (
        merged_df.groupby('product_id').agg(
            total_sales_amount=('sale_price', 'sum'), 
            total_units_sold=('units', 'sum')).reset_index()
    )

    result['average_price'] = result['total_sales_amount'] / result['total_units_sold']
    result['average_price'] = result['average_price'].where(result['total_units_sold'] != 0, 0).round(2)
    return result[['product_id', 'average_price']]

testCases = [
           {
        "prices": [
            [1, '2023-01-01', '2023-01-31', 10],
            [2, '2023-01-01', '2023-01-31', 20]
        ],
        "units_sold": [],  
        "expected": [
            {"product_id": 1, "average_price": 0},
            {"product_id": 2, "average_price": 0}
        ]
    },
    {
        "prices": [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30]],
        "units_sold": [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]],
        "expected": [
            {"product_id": 1, "average_price": 6.96}, 
            {"product_id": 2, "average_price": 16.96}]
    },
]

for i, testcase in enumerate(testCases):
    prices = pd.DataFrame(testcase["prices"], columns=['product_id', 'start_date', 'end_date', 'price']).astype({'product_id':'Int64', 'start_date':'datetime64[ns]', 'end_date':'datetime64[ns]', 'price':'Int64'})
    units_sold = pd.DataFrame(testcase["units_sold"], columns=['product_id', 'purchase_date', 'units']).astype({'product_id':'Int64', 'purchase_date':'datetime64[ns]', 'units':'Int64'})
    output = average_selling_price(prices, units_sold)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")