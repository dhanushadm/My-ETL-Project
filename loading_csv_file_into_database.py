import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv('data.csv', encoding='ISO-8859-1')
engine = create_engine('postgresql+psycopg2://postgres:abcd1234@localhost:5432/my_database')
df.to_sql('my_table',con=engine,if_exists='replace',index=False)
print("CSV loaded to database successfully!")