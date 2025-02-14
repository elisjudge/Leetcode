import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    start_df = activity[activity["activity_type"] == "start"].rename(columns={"timestamp": "start_time"})
    end_df = activity[activity["activity_type"] == "end"].rename(columns={"timestamp": "end_time"})

    merge_df = pd.merge(
        start_df[["machine_id", "process_id", "start_time"]],
        end_df[["machine_id", "process_id", "end_time"]],
        how="inner",
        on= ["machine_id", "process_id"])
    
    merge_df["process_time"] = merge_df["end_time"] - merge_df["start_time"]

    result = merge_df.groupby("machine_id")["process_time"].mean().round(3).reset_index()
    result.rename(columns={"process_time": "processing_time"}, inplace=True)
    return result



testCases = [
    {
        "activity": [[0, 0, 'start', 0.712], [0, 0, 'end', 1.52], [0, 1, 'start', 3.14], [0, 1, 'end', 4.12], [1, 0, 'start', 0.55], [1, 0, 'end', 1.55], [1, 1, 'start', 0.43], [1, 1, 'end', 1.42], [2, 0, 'start', 4.1], [2, 0, 'end', 4.512], [2, 1, 'start', 2.5], [2, 1, 'end', 5]],
        "expected": [{"machine_id": 0, "processing_time": 0.894}, {"machine_id": 1, "processing_time": 0.995}, {"machine_id": 2, "processing_time": 1.456}]
    }
]

for i, testcase in enumerate(testCases):
    activity = pd.DataFrame(testcase["activity"], columns=['machine_id', 'process_id', 'activity_type', 'timestamp']).astype({'machine_id':'Int64', 'process_id':'Int64', 'activity_type':'object', 'timestamp':'Float64'})
    output = get_average_time(activity)
    if output.to_dict(orient='records') == testcase["expected"]:
        print(f"Test Case {i} Passed.") 
    else:
        print(f"Test Case {i} Failed.")
    print(f" Expected: {testcase['expected']}")
    print(f"Result: {output.to_dict(orient='records')}")