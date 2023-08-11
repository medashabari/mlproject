import logging 
import os 
import datetime 

# log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# log file dir
LOGS_PATH_DIR = os.path.join(os.getcwd(),"logs")
os.makedirs(LOGS_PATH,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOGS_PATH_DIR,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)