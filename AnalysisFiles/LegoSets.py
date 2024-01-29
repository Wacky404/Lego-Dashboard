import pandas as pd
import os.path
import os

data_lego = os.path.join(os.pardir, 'LEGOSETS', r'lego_sets.csv')
data_dictionary = os.path.join(
    os.getcwd(), 'LEGOSETS', r'lego_sets_data_dictionary.csv')


def df_year(df):
    df = df.copy()
    while True:
        try:
            user_input = int(input('Year Release?: '))
            if len(str(user_input)) == 4:
                # to filiter based on word/input
                df_out = df.loc[df['Year'] == user_input]
                return df_out
            else:
                raise Exception
        except Exception:
            print('Pleae input a integer value')


def df_theme(df):
    df = df.copy()
    while True:
        try:
            user_input = input('Theme?: ')
            # to filiter based on word/input
            if isinstance(user_input, str):
                df_out = df.loc[df['Theme'] == user_input]
                return df_out
            else:
                raise Exception
        except Exception:
            print('Pleae input a string')


def df_price_range(df):
    df = df.copy()
    while True:
        try:
            user_input = int(input('Price?: '))
            if user_input is not None:
                # to filiter based on word/input
                df_out = df.loc[df['Retail Price'] >= user_input]
                return df_out
            else:
                raise Exception
        except Exception:
            print('Pleae input a integer value')


if __name__ == '__main__':
    # Going to do some data wrangling in this file to export dfs into visualization
    df = pd.read_csv(data_lego)
    df.columns = ['ID', 'Name', 'Year', 'Theme', 'Subtheme', 'Grouptheme',
                  'Category', 'Pieces', 'Minifigs', 'Agerange_min',
                  'Retail Price', 'Set url', 'Thumbnail url', 'Image url']

    print('Min: ', df['Retail Price'].min())
    print('Max: ', df['Retail Price'].max())
    print(df_price_range(df))
