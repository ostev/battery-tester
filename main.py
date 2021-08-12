import time
from math import ceil
from time import sleep

def prev_sample_time():
    prev_time = None
    try:
        file = open("/prev_time", "r")
        prev_time = int(file.read())
        print("file" + file.read())
        file.close()
    except:
        prev_time = int(time.time()) - 1000000000
    return prev_time

def next_sample_time(prev_time):
    next = (ceil(prev_time / 60) * 60) + 60
    return next

def wait_until_next_sample_time():
    print(time.time())
    prev = prev_sample_time()
    next = next_sample_time(prev)
    print("prev " + str(prev))
    print(next)
    print(str(next - prev)) # TODO: Why is this negative?
    sleep(next - prev)
    # sleep(1)

    file = open("/prev_time", "w")
    file.write(str(next))
    file.close()

def main():
    while True:
        wait_until_next_sample_time()
        print("sample")
        sleep(0.999)

main()