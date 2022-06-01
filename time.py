import schedule
import time


def job(t):
    print("I'm working...")
    return


schedule.every().day.at("01:00").do(job, 'It is 01:00')


def geeks():
    print("Shaurya says Geeksforgeeks")


def geeks2():
    print("Shaurya says Geeksforgeeksfdfsdfdss")


schedule.every(1).minutes.do(geeks)
schedule.every(2).seconds.do(geeks2)


while True:
    schedule.run_pending()

    time.sleep(1)  # wait one minute
