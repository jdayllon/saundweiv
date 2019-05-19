#!/usr/bin/env python
from os import listdir
from os.path import isfile, join
import pickle
import os
from loguru import logger


def diff(l1, l2):
    return list(set(l2) - set(l1))

logger.info("Running")
WORK_DIR = os.environ['WORK_DIR']
cur_files = [f for f in listdir(WORK_DIR) if isfile(join(WORK_DIR, f))]

try:
    last_files_pickle = open('/tmp/workdir_files.pickle','rb')
    last_files = pickle.load(last_files_pickle)
    last_files_pickle.close()

    logger.info("Compare Work Dir")
    if len(diff(cur_files, last_files)) > 0 or len(diff(last_files, cur_files)) > 0:
        logger.warning("Changes found, restarting Frontail")
        os.system("pkill -f frontail")
        os.system("/root/run_trail.sh")
except:
    pass

# Write status
logger.info("Writing current dir status")
cur_files_pickle = open('/tmp/workdir_files.pickle','wb')
pickle.dump(cur_files, cur_files_pickle)
cur_files_pickle.close()

