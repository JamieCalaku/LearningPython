import time

# Exercise 1 from lesson 19
# The task is to make a timer that prints every second in the console

timer = int(input("How long should the timer be (in seconds)?: "))

for x in range(timer, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")