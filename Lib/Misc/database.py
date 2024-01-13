from .json import *
from .logs import *
import mysql.connector

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
    
def init_database(db_name, db_config_file):
    config = get_json_content(db_config_file)
    if config == -1: 
        write_json(db_config_file, {'host': 'localhost', 'user': 'smartswap', 'pass': 'null'})
        print(f"{db_config_file} has been created.")
        exit()
    return DatabaseSQL(
        config["host"],
        config["user"],
        config["pass"],
        db_name
        )
