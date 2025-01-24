import sqlite3
import os

db_file = '1068.db'
schema_file = '1068_Schema.sql'
solution_file = '1068_Solution.sql' 

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

    expected_result = [("Nokia", 2008, 5000,), ("Nokia", 2009, 5000,), ("Apple", 2011, 9000,)]  

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
