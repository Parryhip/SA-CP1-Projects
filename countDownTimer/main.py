#Samuel Andelin, Count Down Timer RAID
import time
amount_of_seconds = int(input("How many seconds do you want the timer to be?"))
print("Timer started!")
while True:
    print(amount_of_seconds)
    amount_of_seconds -= 1
    time.sleep(1)
    if amount_of_seconds == 0:
        print("Time's up!!!")
        break
