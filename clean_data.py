# Gavin Daves, INDE 577, Rice University, Dr. Randy Davila
# Cleaning the Spotify dataset for use in notebooks

# Imports
import pandas as pd
import numpy as np
import os

os.chdir('../../')

def clean_data(df):
    """
    Cleans the Spotify dataset for use in the notebooks.
    Args:
        df: the Spotify dataset
    Returns:
        df: the cleaned Spotify dataset
    """

    # Removing duplicate songs
    df = df.drop_duplicates(subset='track_name')
    
    # Drop the rows with missing values
    df = df.dropna()
    
    # Edit the artists to only include the first artist (remove everything after the first ;)
    df['artists'] = df['artists'].str.split(';', expand=True)[0]
    
    return df

def get_df():
    """
    Returns the df to retrieve from other files.
    Returns:
        df: the cleaned Spotify dataset
    """
    
    df = pd.read_csv('spotify_data.csv')
    df = clean_data(df)
    return df
