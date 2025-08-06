# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)

import threading
import time

def walk_dog(name):
    time.sleep(8)
    print(f"You finish walking {name}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

# These Tasks all run on the same thread, so the tasks will be completed one by one
'''
walk_dog()
take_out_trash()
get_mail()
'''

# Instead, you can use multiple threads, to run multiple tasks at once
# Creating Threads
chore1 = threading.Thread(target=walk_dog, args=("Buddy",))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()


# Join method prevents the code from continuing although the threads aren't completed
chore1.join()
chore2.join()
chore3.join()

print("All Chores are complete")