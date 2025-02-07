import os 
import sys 
from decouple import config 
MAIN_PATH = config('MAIN_PATH')
sys.path.insert(1, MAIN_PATH)

from offline_testing.analysis.custom_statistics import get_summary_stats, read_file

ALGO = "custom"

# First we quickly check and verify that the RL experiments have properly completed based on the 
# general template/guidelines used. You can customise additional parameters, check func "experiment_error_check".
# experiment_error_check(cohort="child", algorithm=ALGO, algoAbbreviation=ALGO)
# experiment_error_check(cohort="child", algorithm='SAC', algoAbbreviation='SAC')



# get_summary_stats(experiment_name="CustomTest1",cohort="child", algo_type=ALGO, algorithm=ALGO, algoAbbreviation=ALGO, 
#                   metric=['50%', '25%', '75%','mean', 'std'], 
#                   verbose=False, show_res=True, sort=[False, 'hgbi'])

# print("Done")

data = read_file(experiment_name="CustomTest1", algorithm=ALGO, n_trials=2, base_num=5000)

for nums in data:
    print("worker_episode_",nums,sep='')
    for c,episode_data in enumerate(data[nums]):
        print("\tEpisode",c+1)
        for k in episode_data:
            print("\t\t",k,':',','.join([str(round(float(i),2)) for i in episode_data[k]]))
        print()