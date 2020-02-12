import pandas as pd

def add_df(x, y):
    df = pd.DataFrame([[x, y]], columns=['first', 'second'])
    result = float(df['first'].iloc[0]) + float(df['second'].iloc[0])
    return result
