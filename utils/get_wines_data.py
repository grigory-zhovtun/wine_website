"""Module for retrieving and processing wine data from an Excel file."""
import os
import pandas as pd
import argparse
from dotenv import load_dotenv


def get_wines_data():
    """
    Retrieve wine data from an Excel file and structure it by category.

    This function reads wine data from an `.xlsx` file, processes it,
    and returns the data as a dictionary where wines are grouped by
    their categories.

    Returns:
        list: A list of dictionaries where each dictionary represents
        a wine category and its associated wines in the following format:
        [
            {
                "Category Name": [
                    {
                        "name": "Wine Name",
                        "grape_variety": "Grape Variety",
                        "price": "Price",
                        "image": "Image Filename",
                        "promotion": "Special Price"
                    }
                ]
            }
        ]
    """
    load_dotenv()

    excel_file_path = os.environ.get("EXCEL_FILE_PATH")
    if not excel_file_path:
        raise ValueError("EXCEL_FILE_PATH must be provided in the environment variables.")

    parser = argparse.ArgumentParser(description="Get wine data from an Excel file")
    parser.add_argument(
        "--path_to_excel_file",
        type=str,
        default=excel_file_path,
        help="Path to excel file with wine data.",
    )
    args = parser.parse_args()

    wines_data = pd.read_excel(args.path_to_excel_file)
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
