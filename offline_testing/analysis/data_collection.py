import os

TRIAL_DIGIT_NUM = 3
CSV_HEADERS = ["Step","Glucose", "CGM", "t", "CHO", "Insulin", "MA"]
DEFAULT_FILE_NAME = "TRIAL_"
LOGS_DEFAULT = True

def int_show(num, force_digits=3):
    str_num = str(num)
    return '0'*max(0, force_digits - len(str_num)) + str_num

def get_next_file_num(folder_dest, starts_with=""): #assumes all csv files in folder end with 
    files = os.listdir(folder_dest)
    start_len = len(starts_with)
    numbers = [0] + [int(file.split('.')[0][-3:]) for file in files if (file[:start_len] == starts_with)]
    print("Files:",files)
    print("Numbers:", numbers)
    return int_show(max(numbers) + 1, TRIAL_DIGIT_NUM)


def write_summary_md(mem_obj, agent_name, file_dest):
    pass

def write_csv(mem_obj, folder_dest, logs=LOGS_DEFAULT):
    lines = [','.join(CSV_HEADERS)]
    data = mem_obj.get_simu_data()

    sim_len = len(data[0])
    for n in range(sim_len):
        lines.append(','.join([str(n)] + [str(float(i[n][0])) for i in data]))

    file_name = DEFAULT_FILE_NAME + get_next_file_num(folder_dest) + ".csv"

    with open(folder_dest+file_name,'w') as f:
        f.write('\n'.join(lines))
    
    if logs:
        print("CSV File", folder_dest + file_name,"written.")

    


if __name__ == "__main__":
    get_next_file_num("data/trials/default/")