import json
import time

def get_prev_time():
    prev_time = None
    try:
        file = open("/prev_time", "r")
        prev_time = file.read()
    except:
        prev_time = time.time()
    
    return prev_time