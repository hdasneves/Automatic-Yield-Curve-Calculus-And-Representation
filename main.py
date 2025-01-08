import import_data
import pandas as pd
import numpy as np
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt


def handle_data(date : str):
    data = import_data.get_data(date)

    if data.empty :
        print("Erreur lors de l'import des données.") 
        return None
    
    data["Date"] = pd.to_datetime(data["Date"])
    data.sort_values(by = 'Date', inplace = True, ignore_index = True)
    closest_index = (data['Date'] - pd.to_datetime(date)).abs().idxmin()

    get_graph(data.iloc[closest_index].to_dict())

def get_graph(final_dict : dict):
    axis_x_data = list(final_dict.keys())[1:]
    axis_y_data = list(final_dict.values())[1:]

    plt.figure(figsize=(12, 6))
    sns.lineplot(x = axis_x_data, y = axis_y_data)
    plt.title(f"Courbe des taux le {str(final_dict['Date'])[0:10]}")
    plt.legend(["Courbe des taux"], loc = "upper left")
    plt.xlabel("Maturities")
    plt.ylabel("Rates (%)")
    plt.show()


final_dict = handle_data("2025-01-08")