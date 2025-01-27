import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(players.shape)


testCases = [
    {
        "data": [
            {"player_id": 846, "name": "Mason", "age": 21, "position": "Forward", "team": "RealMadrid"},
            {"player_id": 749, "name": "Riley", "age": 30, "position": "Winger", "team": "Barcelona"},
            {"player_id": 155, "name": "Bob", "age": 28, "position": "Striker", "team": "ManchesterUnited"},
            {"player_id": 583, "name": "Isabella", "age": 32, "position": "Goalkeeper", "team": "Liverpool"},
            {"player_id": 388, "name": "Zachary", "age": 24, "position": "Midfielder", "team": "BayernMunich"},
            {"player_id": 883, "name": "Ava", "age": 23, "position": "Defender", "team": "Chelsea"},
            {"player_id": 355, "name": "Violet", "age": 18, "position": "Striker", "team": "Juventus"},
            {"player_id": 247, "name": "Thomas", "age": 27, "position": "Striker", "team": "ParisSaint-Germain"},
            {"player_id": 761, "name": "Jack", "age": 33, "position": "Midfielder", "team": "ManchesterCity"},
            {"player_id": 642, "name": "Charlie", "age": 36, "position": "Center-back", "team": "Arsenal"},
        ],
        "expected": [10, 5]
    }
]

for i, testcase in enumerate(testCases):
    output = getDataframeSize(pd.DataFrame(testcase["data"]))

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")