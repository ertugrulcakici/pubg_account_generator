class Logger:
    def __init__(self, printing: bool = True):
        self.printing = printing
        if not self.printing:
            self.logfile = open("log.txt", "w")

    def log(self, msg):
        if self.printing:
            print(msg)
        else:
            self.logfile.write(msg + "\n")
