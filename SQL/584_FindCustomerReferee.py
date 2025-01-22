import sqlite3
import os

db_file = '584.db'
schema_file = '584_Schema.sql'
solution_file = '584_Solution.sql' 


# Create a connection to the SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Function to load and execute SQL from a file
def execute_sql_file(filename):
    with open(filename, 'r') as file:
        sql = file.read()  # Read the entire SQL from the file
        cursor.executescript(sql)  # Execute the SQL script

# Function to run the test case and compare results
def test_case():
    with open(solution_file, 'r') as file:
        solution_query = file.read()

    cursor.execute(solution_query)
    result = cursor.fetchall()

    expected_result = [("Will",), ("Jane",), ("Bill",), ("Zack",)]  

    if result == expected_result:
        print("Test Case Passed")
        print(f"Expected: {expected_result}")
        print(f"Got: {result}")
    else:
        print("Test Case Failed")
        print(f"Expected: {expected_result}")
        print(f"Got: {result}")

def main():
    execute_sql_file(schema_file) 

    test_case()

    cursor.close()
    conn.close()

    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Database file '{db_file}' deleted successfully.")

if __name__ == "__main__":
    main()
