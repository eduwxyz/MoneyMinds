import configparser
from pathlib import Path

from moneyminds import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath("." + Path.home().stem + "_moneyminds.json")

def get_database_path(config_file: Path):
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return config_parser["General"]["database"]


def init_database(db_path: Path):
    try:
        db_path.write_text("[]")
        return SUCCESS
    
    except FileExistsError:
        return DB_WRITE_ERROR
    