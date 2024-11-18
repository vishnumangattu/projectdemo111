import random
from datetime import datetime

# Open log.txt to append a contribution entry
with open("log.txt", "a") as file:
    # 70% chance to skip contributions on some days
    if random.random() < 0.98:
        file.write(f"No contribution on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("No contributions today!")
    else:
        # Random number of contributions (between 1 and 5)
        num_contributions = random.randint(3, 9)
        for _ in range(num_contributions):
            file.write(f"Contribution on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"{num_contributions} contributions made today!")
