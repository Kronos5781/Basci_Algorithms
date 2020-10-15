import time

class StopClock:

    def __init__(self):
        self.start = None
        self.end = None

    def start_clock(self):
        self.start = time.time()

    def stop_clock(self, process):
        self.end= time.time()
        print("Time Lapsed for " + process + " = {0}".format(self.end - self.start))