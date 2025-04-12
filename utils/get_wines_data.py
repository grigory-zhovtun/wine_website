"""Module for retrieving and processing wine data from an Excel file."""
import pandas as pd


def get_wines_data(excel_file_path):
    """
    Retrieve wine data from an Excel file and structure it by category.

    This function reads wine data from an `.xlsx` file, processes it,
    and returns the data as a dictionary where wines are grouped by
    their categories.

    Args:
        excel_file_path: Path to the `.xlsx` file.

    Returns:
        list: A list of dictionaries where each dictionary represents
        a wine category and its associated wines
    """
    wines_data = pd.read_excel(excel_file_path)
    wines_data = wines_data.fillna('')
    wines_data.columns = [
        'category', 'name', 'grape_variety', 'price', 'image', 'promotion'
    ]

    wines_data_transformed = {}
    for row in wines_data.to_dict(orient='records'):
        wines_data_transformed.setdefault(row['category'], []).append(row)

    sorted_wines_data_transformed = {
        key: wines_data_transformed[key] for key in sorted(wines_data_transformed)
    }

    return sorted_wines_data_transformed
