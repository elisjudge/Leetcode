import sqlite3
import os

db_file = '1581.db'
schema_file = '1581_Schema.sql'
solution_file = '1581_Solution.sql' 

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

def execute_sql_file(filename):
    with open(filename, 'r') as file:
        sql = file.read()  
        cursor.executescript(sql)  

def test_case():
    with open(solution_file, 'r') as file:
        solution_query = file.read()

    cursor.execute(solution_query)
    result = cursor.fetchall()

    expected_result = [(54, 2, ), (30, 1, ), (96, 1, )]  

    if sorted(result) == sorted(expected_result):
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
