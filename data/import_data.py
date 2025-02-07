import os
import torch
import numpy as np
import csv
import pandas as pd
from datetime import datetime
import sys
import pickle

AGE_VALUES = ["adolescent", "adult"]
MODEL_TYPES = ["A2C", "AUXML", "BBHE", "BBI", "G2P2C", "PPO", "SAC"]

FOLDER_TYPE_MODELS = ["A2C", "AUXML", "G2P2C", "PPO", "SAC"]
CSV_TYPE_MODELS = ["BBHE", "BBI"]

OBJECT_SAVE_FILE = "../data" + "/object_save/data_dictionary.pkl"


EXCLUDE_FILES = ["quadratic.csv", "real.csv"]
def import_all_data(
        dest="../data", 
        age_range = AGE_VALUES,
        model_range = MODEL_TYPES,
        csv_type_list = CSV_TYPE_MODELS,
        folder_type_list = FOLDER_TYPE_MODELS
        ):
    
    data_dict = dict() #consider file type for this! will be very slow

    for age in age_range:
        data_dict[age] = dict()
        for model in model_range:
            model_folder = dest + '/' + age + '/' + model + '/'
            print(model_folder)
            if model in csv_type_list:
                data_dict[age][model] = []

                available_files = os.listdir(model_folder)

                for excl_file in EXCLUDE_FILES:
                    if excl_file in available_files: 
                        available_files.remove(excl_file)
                        print("\t>>Excluded",excl_file,"from",model_folder)

                for file in available_files:
                    file_dest = model_folder + file
                    print('\t' + file_dest)
                    data_dict[age][model].append(import_from_csv(file_dest))

                # data_dict[age][model] = np.array(data_dict[age])


            elif model in folder_type_list:
                available_folders = os.listdir(model_folder)
                data_dict[age][model] = []
                for folder in available_folders:
                    folder_dest = model_folder + folder
                    print('\t' + folder_dest)
                # data_dict[age][model] = np.array(data_dict)

    return data_dict

CSV_HEADERS = ["CGM", "meal", "ins", "t"]
def import_from_csv(file_dest, headers=CSV_HEADERS): #imports data from a csv file
    df = pd.read_csv(file_dest, header=None, names=headers)
    data_dict = {col: df[col].to_numpy(dtype=float) for col in headers}
    return data_dict

def import_from_obj(file_dest=OBJECT_SAVE_FILE):
    with open(file_dest, 'rb') as f:
        data_dict = pickle.load(f)
    return data_dict

def save_to_obj_file(data_dict, file_dest=OBJECT_SAVE_FILE):
    with open(file_dest, 'wb') as f:
        data_dict = pickle.dump(data_dict, f)
    return data_dict

    
SAVE_TO_PICKLE = True
READ_FROM_PICKLE = False
if __name__ == "__main__":
    if READ_FROM_PICKLE:
        start_time = datetime.now()

        file_dest="data/object_save/data_dictionary.pkl"
        data = import_from_obj(file_dest)

        end_time = datetime.now()
        duration = end_time - start_time
        print("Executed in",duration.total_seconds(), "seconds")
        file_size = os.path.getsize(file_dest)
        print(f"Read file has size {file_size / (1024 * 1024):.2f}MB")
    else:
        start_time = datetime.now()
        file_dest="data/object_save/data_dictionary.pkl"
        
        data = import_all_data("data")
        # print(import_from_csv("data/adult/BBI/logs_worker_20_0.csv"))
        print("\nSuccesfully imported.")

        end_time = datetime.now()
        duration = end_time - start_time
        print("Executed in",duration.total_seconds(), "seconds")

        obj_size = sys.getsizeof(data)
        obj_size_mb = obj_size / (1024 ** 2)
        print("Returned object is",round(obj_size_mb,10),"MB")
        for age_k in data:
            print("Age:",age_k)
            for model_k in data[age_k]:
                print("\tModel:", model_k, "with length", len(data[age_k][model_k]))
        
        save_to_obj_file(data, file_dest)
        file_size = os.path.getsize(file_dest)
        print(f"Object saved to {file_dest} with size {file_size / (1024 * 1024):.2f}MB")
        

