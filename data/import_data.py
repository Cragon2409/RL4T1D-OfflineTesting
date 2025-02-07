import os
import torch
import numpy as np
import csv
import pandas as pd
import time

AGE_VALUES = ["adolescent", "adult"]
MODEL_TYPES = ["A2C", "AUXML", "BBHE", "BBI", "G2P2C", "PPO", "SAC"]

FOLDER_TYPE_MODELS = ["A2C", "AUXML", "G2P2C", "PPO", "SAC"]
CSV_TYPE_MODELS = ["BBHE", "BBI"]


def import_all_data(
        dest="../data", 
        age_range = AGE_VALUES,
        model_range = MODEL_TYPES,
        csv_type_list = CSV_TYPE_MODELS,
        folder_type_list = FOLDER_TYPE_MODELS
        ):
    
    data_dict = dict() #consider file type for this! will be very slow

    for age in age_range:
        data_dict[age] = np.array([])
        for model in model_range:
            model_folder = dest + '/' + age + '/' + model + '/'
            print(model_folder)
            if model in csv_type_list:
                available_files = os.listdir(model_folder)
                for file in available_files:
                    file_dest = model_folder + file
                    print('\t' + file_dest)
                    data_dict[age].append(import_from_csv(file_dest))

            elif model in folder_type_list:
                available_folders = os.listdir(model_folder)
                for folder in available_folders:
                    folder_dest = model_folder + folder
                    print('\t' + folder_dest)

    return data_dict

CSV_HEADERS = ["CGM", "meal", "ins", "t"]
def import_from_csv(file_dest, headers=CSV_HEADERS): #imports data from a csv file
    df = pd.read_csv(file_dest, header=None, names=headers)
    data_dict = {col: df[col].to_numpy(dtype=float) for col in headers}
    return data_dict
    

if __name__ == "__main__":
    start_time = time.perf_counter()
    data = import_all_data("data")
    # print(import_from_csv("data/adult/BBI/logs_worker_20_0.csv"))
    print("\nSuccesfully imported.")

    end_time = time.perf_counter()
    duration = start_time - end_time
    print("Executed in",round(end_time,3), "seconds")
