import argparse
import sqlite3

def search_vacant_houses(location, bedrooms, price_range):
    # Connect to the SQLite database
    conn = sqlite3.connect("realestate.db")
    cursor = conn.cursor()

    # Build the SQL query based on the provided criteria
    query = "SELECT * FROM houses WHERE location = ?"
    parameters = [location]

    if bedrooms is not None:
        query += " AND bedrooms = ?"
        parameters.append(bedrooms)

    if price_range is not None:
        query += " AND price >= ? AND price <= ?"
        min_price, max_price = map(float, price_range.split('-'))
        parameters.extend([min_price, max_price])

    # Execute the query
    cursor.execute(query, parameters)

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(f"House ID: {row[0]}, Location: {row[1]}, Bedrooms: {row[2]}, Price: {row[3]}")

    # Close the connection
    conn.close()

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Search for vacant houses in a town.")

    # Define command-line arguments
    parser.add_argument("location", help="The town or location to search in")
    parser.add_argument("--bedrooms", type=int, default=None, help="Number of bedrooms (optional)")
    parser.add_argument("--price-range", help="Price range (optional)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the search function with the provided arguments
    search_vacant_houses(args.location, args.bedrooms, args.price_range)

if __name__ == "__main__":
    main()
