import pandas as pd
import os


def get_wines_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', 'product_data', 'wine3.xlsx')

    wines_data = pd.read_excel(file_path)
    wines_data = wines_data.fillna('')
    wines_data.columns = ['category', 'name', 'grape_variety', 'price', 'image', 'promotion']

    wines_data_transformed = {}
    for row in wines_data.to_dict(orient='records'):
        wines_data_transformed.setdefault(row['category'], []).append(row)

    sorted_wines_data_transformed = {
        key: wines_data_transformed[key]
        for key in sorted(wines_data_transformed)
    }

    return sorted_wines_data_transformed