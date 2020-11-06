from datetime import datetime
import os
import json
import shutil
from distutils.dir_util import copy_tree


BASE_DIR = os.getcwd()
CONFIG_FILE = "{}/config.json".format(BASE_DIR)
with open(CONFIG_FILE) as file:
    config = json.load(file)

try:
    LIMIT = int(config["LIMIT"])
except ValueError:
    raise ValueError("Enter a valid number for limit in config.json")
HISTORY = config["HISTORY"]
BACKUP_DIR = config["BACKUP_DIR"]
DATABASE= config["DATABASE"]
URI = config["URI"]
HISTORY_FILE = BASE_DIR + "/" + HISTORY

# create mongodump
mongo_dump = "mongodump --uri {}".format(URI)
os.system(mongo_dump)

# create next backup directory
curr_time = datetime.now()
temp = BASE_DIR + "/" + BACKUP_DIR
os.chdir(temp)
next_backup_dir = str(curr_time.date())+"_"+str(curr_time.time())
os.mkdir(next_backup_dir)

# copy new data to newly created folder
from_dir = BASE_DIR + "/dump/" + DATABASE
next_backup_dir = str(os.getcwd()) + "/" + next_backup_dir
copy_tree(from_dir, next_backup_dir)

# find old folder beyond limit, needs to be deleted
curr_dir_files = os.listdir(temp)
curr_dir_files = sorted(curr_dir_files, reverse=True)
counter = 0
to_remove_dir = list()
for file in curr_dir_files:
    if os.path.isdir(file):
        if counter >= LIMIT:
            to_remove_dir.append(file)
        else:
            counter += 1
print("dir to remove => ", to_remove_dir)

# delete old folder
with open(HISTORY_FILE, 'a') as log:
    for _ in to_remove_dir:
        log.write(_)
        log.write('  ==> {} \n'.format(datetime.now()))
        shutil.rmtree(_)
