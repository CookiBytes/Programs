import time

print("Pick a time from 10 to 50, all in numbers like 20, 30, etc.")
pick = input(">> ")


def countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
        if n == 0:
            print("Ended Countdown!")


if pick == "10":
    countdown(10)

if pick == "20":
    countdown(20)

if pick == "30":
    countdown(30)

if pick == "40":
    countdown(40)

if pick == "50":
    countdown(50)
