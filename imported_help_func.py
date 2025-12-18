import pandas as pd

def get_list(column_name):
  csv_path="survey_data.csv"

  df=pd.read_csv(csv_path)

  if column_name in df.columns:
          return df[column_name]
  else:
         raise ValueError("Column are not found in the DataFrame")

         
