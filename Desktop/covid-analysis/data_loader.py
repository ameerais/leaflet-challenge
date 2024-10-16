
import pandas as pd

def load_data(file_path):
    """
    Load the dataset from a specified path.
    
    Args:
    file_path (str): URL or local file path to the dataset.

    Returns:
    pd.DataFrame: Loaded dataset as a DataFrame.
    """
    try:
        print(f"Loading data from: {file_path}")
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully with {len(data)} records.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """
    Clean the loaded dataset by filtering and preparing necessary columns.

    Args:
    df (pd.DataFrame): Raw data.

    Returns:
    pd.DataFrame: Cleaned dataset.
    """
    print("Cleaning data...")
    if df is not None:
        cleaned_df = df[['Condition', 'Deaths']].dropna()
        print(f"Data cleaned. {len(cleaned_df)} records remaining after cleaning.")
        return cleaned_df
    else:
        print("No data to clean.")
        return None
