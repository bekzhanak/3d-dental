import sys

from sqlalchemy import create_engine, text

# Define the connection string
server = '192.168.0.103'  # e.g., 'localhost' or '192.168.1.1'
database = 'user_net'  # The name of your database
username = 'bekzhan'  # Your SQL Server username
password = 'beka2345'  # Your SQL Server password

# Create the connection string
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

data_txt = "previous_data.txt"


def extract_data_from_db():
    try:
        with engine.connect() as connection:
            print("Connection successful")
            result = connection.execute(
                text(
                    """SELECT * FROM patient_info JOIN study_info ON patient_info.patient_id = study_info.patient_id"""))
            return result.fetchall()
    except Exception as e:
        print("Connection failed:", e)
        sys.exit()


def extract_new_data():

    result = extract_data_from_db()
    new_data = set(tuple(row) for row in result)

    prev_data = set()
    with open(data_txt) as file:
        for row in file:
            prev_data.add(tuple(row.strip().split()))

    difference = new_data - prev_data

    if difference:
        write_new_data_to_txt(difference)

    return difference


def write_new_data_to_txt(difference: set):
    with open(data_txt, 'a') as file:
        for record in difference:
            file.write(" ".join(map(str, record)) + "\n")
