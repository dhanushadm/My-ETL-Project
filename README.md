# My-ETL-Project
This project automates the process of getting raw data, changing it, and saving it in a database. It checks for a JSON file, converts it into a CSV file, and loads it into a PostgreSQL database. The whole process runs every 2 minutes using Python, making it automatic and error-free.

# Architecture 

![Blank diagram](https://github.com/user-attachments/assets/17213b48-4cc6-4240-b76f-2e2c18492e06)

# Table 

![Screenshot (94)](https://github.com/user-attachments/assets/f68c8be4-fcbd-4e6c-92df-a4d74e1971b4)

# Technology Stack

**Python**: Used for writing the ETL scripts to extract, transform, and load data. Python fetches data from APIs, processes it, and saves it in different formats like JSON and CSV.

**PostgreSQL**: A database used to store the transformed data. It keeps the data organized and ready for analysis.

**SQLAlchemy**: A Python library that helps connect to PostgreSQL and easily insert data into the database.

**Pandas**: A Python library used for reading, manipulating, and transforming data, such as converting CSV files to a format that can be loaded into the database.

**Task Scheduler (Using Python)**: Used to schedule the ETL process to run automatically every 2 minutes, ensuring the workflow is triggered when new files are available.

**os & time (Python libraries)**: Used to monitor file paths and wait until the necessary files are available before moving to the next stage in the ETL process.

**JSON/CSV**: File formats used to store raw and transformed data. JSON is used for raw data, and CSV is used for storing transformed data before loading it into the database.

# Data Source Used
**FakeStoreAPI** -An open-source API that provides product data for e-commerce applications.
