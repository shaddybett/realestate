import sqlite3

# def setup_database():
#     # Connect to or create the SQLite database file
#     conn = sqlite3.connect("realestate.db")

#     # Create a cursor object to execute SQL commands
#     cursor = conn.cursor()

#     # Create a table to store house information
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS houses (
#             id INTEGER PRIMARY KEY,
#             location TEXT NOT NULL,
#             bedrooms INTEGER,
#             price REAL
#         )
#     ''')

#     # Insert some sample data
#     cursor.executemany('''
#         INSERT INTO houses (location, bedrooms, price) VALUES (?, ?, ?)
#     ''', [
#         ('Kayole', 2, 6000),
#         ('Kibera', 1, 1500),
#         ('Mathare',2, 2500),
#     ])

#     # Commit changes and close the connection
#     conn.commit()
#     conn.close()

# if __name__ == "__main__":
#     setup_database()
