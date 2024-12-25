# 1. since it is a small project I'm using a simple method to check the file existence 
# 2. for larger projects or real- world projects we use a dynamic method for folder monitoring using "watchdog" library to ensure better efficiency
import os
import time
import pandas as pd
from sqlalchemy import create_engine
import schedule
import sys

# respective File paths
json_file_path = r"C:\Users\dhanu\OneDrive\Desktop\etl_project\raw_data\data.json"
csv_file_path = r"C:\Users\dhanu\OneDrive\Desktop\etl_project\transformed_data\data.csv"

# Function to check file existence
def wait_for_file(file_path, phase_name):
    while not os.path.exists(file_path):
        time.sleep(5)  # Waiting 5 seconds before checking again
    print(f"{phase_name} - {file_path} found")

# ETL process function
def run_etl():
    # Waitinf for JSON file (raw_data) to start transformation
    wait_for_file(json_file_path, "Transformation phase")

    # Performing Transformation
    print("Running Transformation phase...")   

    # Waiting for CSV file (transformed_data) to start load phase
    wait_for_file(csv_file_path, "Load phase")

    # Performing Load
    print("Running Load phase...")  

    # Loading CSV data into the database
    print("Loading transformed data into the database...")

    # To Read the CSV file
    df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

    # Setting  up the database connection using SQLAlchemy
    engine = create_engine('postgresql+psycopg2://postgres:abcd1234@localhost:5432/my_database')

    # Load the data into the PostgreSQL table
    df.to_sql('my_table', con=engine, if_exists='append', index=False)

    print("Data loaded into the database successfully!")

# Schedule the job to run every 2 minutes
schedule.every(2).minutes.do(run_etl)

# Termination condition: Run for a specific number of iterations
max_runs = 10  # Maximum number of runs
run_count = 0

# Keep the script running to continuously check the schedule
while run_count < max_runs:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
    run_count += 1

print("Maximum run limit reached. Terminating the script.")
sys.exit(0)  # Terminate the script
