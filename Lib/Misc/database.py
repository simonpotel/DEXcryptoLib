import mysql.connector
from .json import *
from .logs import *
from datetime import datetime

class DatabaseSQL(object):
    def __init__(self, host, user, password, database):
        """
        Initializes the class with database connection information.

        Parameters:
        - host: The database host.
        - user: The username for the connection.
        - password: The password for the connection.
        - database: The database name.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    def am_connected(self):
        """
        Return a boolean if am connected to the database.
        """
        return self.connection.is_connected()
    def connect(self):
        """
        Establishes a connection to the database using the provided information.
        """
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
    def disconnect(self):
        """
        Closes the database connection if it is open.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
    def execute_query(self, query):
        """
        Executes an SQL query and returns the results.

        Parameters:
        - query: The SQL query to execute.

        Returns:
        - The results of the query.
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    def get_all_rows_from_table(self, table_name):
        """
        Retrieves all rows from a specified table.

        Parameters:
        - table_name: The name of the table to query.

        Returns:
        - The results of the query to fetch all rows from the table.
        """
        query = f"SELECT * FROM {table_name};"
        return self.execute_query(query)
    def insert_into_table(self, table_name, values):
        """
        Inserts values into the specified table.

        Parameters:
        - table_name: The name of the table to insert values into.
        - values: A dictionary containing values to be inserted.
        """
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['%s'] * len(values))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, tuple(values.values()))
            self.connection.commit()
            log("db", "Insertion successful. (table: " + table_name + ") values: " + str(values))
        except Exception as e:
            log("db", f"Error during insertion: {e}")
            self.connection.rollback()
        finally:
            cursor.close()

    def get_prices_for_day(self, table_name, date):
        """
        Retrieves prices for a specific day.

        Parameters:
        - table_name: The name of the table.
        - date: A list containing [year, month, day].

        Returns:
        - A list of tuples, each containing (datetime, price) for the specified day.
        """
        year, month, day = date
        query = f"SELECT date, price FROM {table_name} WHERE DATE(date) = '{year}-{month}-{day}';"
        results = self.execute_query(query)
        return [(result[0], result[1]) for result in results]

    def get_prices_per_hour_for_day(self, table_name, date):
        """
        Retrieves prices for each hour of a specific day.

        Parameters:
        - table_name: The name of the table.
        - date: A list containing [year, month, day].

        Returns:
        - A list of tuples, each containing (datetime, price) for each hour of the day.
        """
        year, month, day = date
        prices_per_hour = []

        # Construct query to fetch prices for each hour
        for hour in range(24):
            hour_start = f"{year}-{month}-{day} {hour:02d}:00:00"
            hour_end = f"{year}-{month}-{day} {hour:02d}:59:59"
            query = f"SELECT date, AVG(price) FROM {table_name} WHERE date BETWEEN '{hour_start}' AND '{hour_end}';"

            # Execute query and fetch result
            result = self.execute_query(query)
            if result[0][0] is not None:
                prices_per_hour.append((result[0][0], result[0][1]))

        return prices_per_hour
    def get_average_prices_per_day(self, table_name):
        """
        Retrieves the average prices for each day.

        Parameters:
        - table_name: The name of the table.

        Returns:
        - A list of tuples, each containing (date, average_price) for each day.
        """
        query = f"SELECT DATE(date) AS date, AVG(price) AS average_price FROM {table_name} GROUP BY DATE(date);"
        results = self.execute_query(query)
        return results

    
def init_database(db_name, db_config_file):
    config = get_json_content(db_config_file)
    if config == -1: 
        write_json(db_config_file, {'host': 'localhost', 'user': 'smartswap', 'pass': 'null'})
        print(f"{'db.json'} has been created.")
        exit()
    return DatabaseSQL(
        config["host"],
        config["user"],
        config["pass"],
        db_name
        )
