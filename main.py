import time
from math import ceil
from time import sleep

def prev_sample_time():
    prev_time = None
    try:
        file = open("/prev_time", "r")
        prev_time = file.read()
        file.close()
    except:
        prev_time = time.time()
    return prev_time
    

def next_sample_time(prev_time):
    next = ceil(prev_time / 60.0) * 60.0
    return next

def wait_until_next_sample_time():
    prev = prev_sample_time()
    next = next_sample_time(prev)
    print("prev " + str(prev))
    print("next " + str(next))
    print(next - prev)
    sleep(next - prev) # Why does this error?
    # sleep(1)

    file = open("/prev_time", "w")
    file.write(next)

def main():
    while True:
        wait_until_next_sample_time()
        print("sample")

main()