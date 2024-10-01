import time
global time_skip
time_skip = False
def wait(seconds):
    if time_skip == True:
        pass
    else:
        time.sleep(seconds)
    #if time_skip is true, it will not wait for the specified amount of time
    #otherwise it will function as a normal time.sleep statement would