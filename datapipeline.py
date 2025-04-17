import pandas as pd
import numpy as np

df = pd.read_csv('recap_pai2019.csv')
df['%participation_Men'] = 100 - df['%participation_Femme'].str.rstrip('%').astype('float') - df['%participation_Jeune'].str.rstrip('%').astype('float')

# Convert '%participation_Femme' column to numeric (remove '%' sign)
df['%participation_Femme'] = df['%participation_Femme'].str.rstrip('%').astype('float')

# Create a new column 'Rank_Women' based on the rank of the percentage of women in descending order
df['Rank_Women'] = df['%participation_Femme'].rank(ascending=False, method='min').astype('int')

df['%participation_Jeune'] = df['%participation_Jeune'].str.rstrip('%').astype('float')

# Create a new column 'High_Participation_Jeune' based on the condition (> 20%)
df['High_Participation_Jeune'] = df['%participation_Jeune'] > 20
from sqlalchemy import create_engine
# PostgreSQL connection parameters
db_params = {
    'host': 'localhost',
    'database': 'madw',
    'user': 'postgres',
    'password': 'trao',
    
}

# Create a SQLAlchemy engine
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}/{db_params["database"]}')

# Specify the table name
table_name = 'Statistiques participation citoyenne au plan...'

# Load the DataFrame into PostgreSQL
df.to_sql(table_name, engine, if_exists='replace', index=False)

# Close the engine
engine.dispose()

# Display the updated DataFrame
print(df) 