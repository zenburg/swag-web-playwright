import pandas as pd


def get_all_login_data():
    file_path = "test_data/test_data.xlsx"
    df = pd.read_excel(file_path, sheet_name="Sheet1")

    # Convert all rows into list of tuples
    return [tuple(row) for row in df.to_numpy()]