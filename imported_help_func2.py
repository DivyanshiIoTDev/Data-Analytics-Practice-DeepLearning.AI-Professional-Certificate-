import pandas as pd
def get_list(column_name):
    csv_path = "restaurant_data.csv"
    try:
        df = pd.read_csv(csv_path)
        if column_name in df.columns:
            return df[column_name].tolist()
        else:
            raise ValueError("Column are not found in the DataFrame")
    except Exception as e:
        print(f"An error has occured: {e}")
