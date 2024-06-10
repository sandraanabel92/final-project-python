import pandas as pd
import os

def load_data(data_path):

    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path)
    elif data_path.endswith("xlsx"):
        df = pd.read_excel(data_path)
    else:
        raise ValueError("Unsupported file format")
    print("Data loaded successfully")
    return df

def clean_data(df):
    df["price"] = df["price"].replace(r"[\$,]", "", regex = True).astype(float) #Se limpia y convierte la columna de precios a tipo float
    print("Data cleaned Successfully")
    return df

def analyze_data(df):
    print("Basic Data Analysis: ")
    print(df.describe())
    print("\nProducts with highest prices: ")
    highestPrices = df.nlargest(5,"price")
    print(highestPrices)

def save_clean_data(df,outputh_path):
    if outputh_path.endswith(".csv"):
        df.to_csv(outputh_path,index = False)
    elif outputh_path.endswith(".xlsx"):
        df.to_excel(outputh_path,index = False)
    else:
        raise ValueError("Unsupported file format")
    print(f"Clean data saved to {outputh_path}")