import os
import random
from datetime import datetime, timedelta

# Config
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2025, 5, 19)
MAX_COMMITS_PER_DAY = 5  # Random up to 5 commits a day

# Generate random commit days
delta = END_DATE - START_DATE
for i in range(delta.days + 1):
    day = START_DATE + timedelta(days=i)
    num_commits = random.randint(0, MAX_COMMITS_PER_DAY)
    for _ in range(num_commits):
        with open("log.txt", "a") as file:
            file.write(f"Commit on {day.isoformat()}\n")
        os.system(f"git add log.txt")
        os.system(f'git commit --date="{day.isoformat()} 12:00:00" -m "Commit on {day.strftime("%Y-%m-%d")}"')

# Push all
os.system("git push origin main")

