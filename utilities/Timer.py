import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        """Start the timer."""
        self.start_time = time.time()
        # print("Timer started.")

    def end(self, do_print=False, print_prefix=""):
        """End the timer and print the elapsed time."""
        if self.start_time is None:
            print("Timer has not been started.")
            return
        self.end_time = time.time()
        elapsed_time = 1000. * (self.end_time - self.start_time)
        if do_print:
            print(print_prefix, f". Elapsed time: {elapsed_time:.2f} ms")
        return elapsed_time


