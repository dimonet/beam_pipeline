import argparse
from argparse import RawTextHelpFormatter
import os
import json
import sys

def get_options():
    p = argparse.ArgumentParser(description='weather_forecasts',
                                formatter_class=RawTextHelpFormatter)

    p.add_argument('--config_file', action="store", dest="config_file",
                   default="conf.json",
                   help="config: configuration file",
                   required=False)
    options = vars(p.parse_args())


    return options

def read_config_file(config_file: str) -> dict:
    try:
        file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            f'../config/{config_file}')
        with open(file, 'r') as f:
            config = json.load(f)
        return config
    except:
        print("cannot load config file")
        sys.exit(1)