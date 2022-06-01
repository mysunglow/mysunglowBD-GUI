import os
import ftplib
from pathlib import Path
import datetime


class Logger:

    def log(self, logString):
        # dt = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        month = datetime.datetime.now().strftime("%B")
        year = datetime.datetime.now().strftime("%Y")

        dir = os.getcwd()
        dir = os.path.join(dir, 'output')
        if not os.path.exists(dir):
            os.mkdir(dir)

        dir = os.getcwd()
        dir = os.path.join(dir, 'output', year)
        if not os.path.exists(dir):
            os.mkdir(dir)

        dir = os.getcwd()
        dir = os.path.join(dir, 'output', year, month)
        if not os.path.exists(dir):
            os.mkdir(dir)

        logFile = open(f"{dir}/log.txt", "a")
        logFile.write(logString+"\n")
        logFile.close()
