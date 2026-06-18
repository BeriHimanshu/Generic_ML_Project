import logging
import os 
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Creates the 'logs' folder safely

# 3. Combine the logs directory with the filename
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# 4. Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH, 
    level=logging.INFO, 
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)

    