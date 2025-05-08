import pandas as pd

try:
    df = pd.read_csv('sentimentdataset mahibavathi.r.csv', encoding='utf-8')
except UnicodeDecodeError:
    try:
        df = pd.read_csv('sentimentdataset mahibavathi.r.csv', encoding='latin-1')
    except Exception as e:
        print(f"Error loading the file: {e}")
        df = None

if df is not None:
    display(df.head())
    print(df.shape)
    print(df.columns)
