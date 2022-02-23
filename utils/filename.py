from datetime import datetime as dt

def generate_filename() -> str:
    res = dt.today().strftime('%Y%m%d%H%M%S')
    return res