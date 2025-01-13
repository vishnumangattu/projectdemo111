import random
from datetime import datetime, timedelta

def log_contributions():
    
    with open("log.txt", "a") as file:
       
        num_contributions = random.randint(3, 9)
        for _ in range(num_contributions):
            file.write(f"Contribution on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"{num_contributions} contributions made!")

def make_commit_on_random_days():
    
    if random.random() < 0.5:  # 50% chance to make a commit today
        print("Logging contributions today...")
        
      
        num_commits = random.randint(2, 8)
        
        for _ in range(num_commits):
            
            log_contributions()
          
            delay_minutes = random.randint(30, 180)  
            next_commit_time = datetime.now() + timedelta(minutes=delay_minutes)
            print(f"Next commit scheduled for {next_commit_time.strftime('%Y-%m-%d %H:%M:%S')}")


make_commit_on_random_days()
