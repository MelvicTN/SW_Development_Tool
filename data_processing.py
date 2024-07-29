# Load library
import pandas as pd


# df = vehicles_df dataframe referenced in My EDA.ipynb
def preprocessing(df):
    # FE: replace the following model names in the 'model' column

    # `ford f150` (counts=530) with `ford f-150` (counts=2796)
    df['model'] = df['model'].replace('ford f150', 'ford f-150')
    # `ford f250` (counts=339) with `ford f-250` (counts=422)
    df['model'] = df['model'].replace('ford f250', 'ford f-250')
    # `ford f-250 sd` (counts=426) with `ford f-250 super duty` (counts=241)
    df['model'] = df['model'].replace('ford f-250 sd', 'ford f-250 super duty')
    # `ford f250 super duty` (counts=370) with `ford f-250 super duty` (counts=241)
    df['model'] = df['model'].replace('ford f250 super duty', 'ford f-250 super duty')
    # `ford f-350 sd` (counts=295) with `ford f350 super duty` (counts=246)
    df['model'] = df['model'].replace('ford f-350 sd', 'ford f350 super duty')
    

    # rename `ford f350 super duty` (counts=541) to `ford f-350 super duty`
    df['model'] = df['model'].replace('ford f350 super duty', 'ford f-350 super duty')
    # rename `ford f150 supercrew cab xlt` (counts=327) to `ford f-150 supercrew cab xlt`
    df['model'] = df['model'].replace('ford f150 supercrew cab xlt', 'ford f-150 supercrew cab xlt')
    # rename `ford f350` (counts=250) to `ford f-350`
    df['model'] = df['model'].replace('ford f350', 'ford f-350')


    # FE: create two new columns, 'make' and 'model_name', derived from 'model' column
    df[['make', 'model_name']] = df['model'].str.split(' ', n=1, expand=True)



    # MISSING VALUES: replace NaN with zero (0 = not 4wd) in 'is_4wd' column 
    df['is_4wd'] = df['is_4wd'].fillna(0)
    # MISSING VALUES: replace NaN with 'white' in 'paint_color' column
    df['paint_color'] = df['paint_color'].fillna('white')
    # MISSING VALUES: replace NaN with 'median' model year calculation in 'model_year' column
    df['model_year'] = df['model_year'].fillna(df.groupby(['model'])['model_year'].transform('median'))
    # MISSING VALUES: replace NaN with 'mean' odometer calculation in 'odometer' column
    df['odometer'] = df['odometer'].fillna(df.groupby(['model', 'model_year'])['odometer'].transform('mean'))
    # MISSING VALUES: replace NaN with 'median' cylinder calculation in 'cylinders' column
    df['cylinders'] = df['cylinders'].fillna(df.groupby(['model', 'model_year'])['cylinders'].transform('median'))
    # DROP MISSING VALUES: drop rows with missing values in 'cylinders' and 'odometer' columns in df
    df = df.dropna(subset=['cylinders', 'odometer'])



    # 'model_year' column convert datatype from float64 to int32 to get 4-digit year
    df['model_year'] = df['model_year'].astype(int)
    # 'date_posted' column convert value datatype from object to datetime 
    df['date_posted'] = pd.to_datetime(df['date_posted'], format='%Y-%m-%d')


    return df





