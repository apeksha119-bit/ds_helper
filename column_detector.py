import pandas as pd

def column_type_detector(df, threshold=20):
    column_types = {}
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            if df[column].nunique() < threshold:
                column_types[column] = 'categorical'
            else:
                column_types[column] = 'numerical'
        elif pd.api.types.is_object_dtype(df[column]):
            column_types[column] = 'text'
        else:
            column_types[column] = 'unknown'
    return column_types
