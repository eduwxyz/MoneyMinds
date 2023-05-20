import configparser
from pathlib import Path

import typer

from moneyminds import DB_WRITE_ERROR, DIR_ERROR, FILE_ERROR, SUCCESS

CONFIG_DIR_PATH = Path(typer.get_app_dir("moneyminds"))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"

def _init_config_file():
    try:
        CONFIG_DIR_PATH.mkdir(parents=True, exist_ok=True)
        
    except FileExistsError:
        return DIR_ERROR
    
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except FileExistsError:
        return FILE_ERROR
    return SUCCESS
    

def _create_database(db_path: str):
    config_parser = configparser.ConfigParser()
    config_parser["General"] = {"database": db_path}
    
    try: 
        with open(CONFIG_FILE_PATH, "w") as f:
            config_parser.write(f)
            
    except FileNotFoundError:
        DB_WRITE_ERROR
    
    return SUCCESS
    
    
def init_app(db_path: str):
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    database_code = _create_database(db_path)
    if database_code != SUCCESS:
        return database_code
    return SUCCESS
    