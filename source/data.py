import pandas as pd


def get_plot_data():
    df = pd.read_csv("sweat_registers.csv")

    if df['voltage'].dtype == 'object':
        df["voltage"] = df["voltage"].str.replace(',', '-').astype("float")
    if df['weight_initial'].dtype == 'object':
        df['weight_initial'] = df['weight_initial'].str.replace(',', '-').astype("float")
    if df['weight_final'].dtype == 'object':
        df['weight_final'] = df['weight_final'].str.replace(',', '-').astype("float")

    df['sweat_id'] = df['voltage']*0.023/0.011
    df['salt_amount'] = 9*(df['weight_initial']-df['weight_final'])*df['sweat_id']

    return df