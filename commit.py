import random
from datetime import datetime

def log_contributions():
    # Open log.txt to append a contribution entry
    with open("log.txt", "a") as file:
        # Ensure a random number of contributions is made between 3 and 9
        num_contributions = random.randint(3, 9)
        for _ in range(num_contributions):
            file.write(f"Contribution on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"{num_contributions} contributions made!")

# Morning contribution (around 9:00 AM)
morning_time = "09:00"
if datetime.now().strftime("%H:%M") == morning_time:
    print("Logging morning contributions...")
    log_contributions()

# Evening contribution (around 6:00 PM)
evening_time = "18:00"
if datetime.now().strftime("%H:%M") == evening_time:
    print("Logging evening contributions...")
    log_contributions()

