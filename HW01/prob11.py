import random

def experiment():
    birthdays = [random.randint(1, 365) for _ in range(50)]
    
    return len(birthdays) != len(set(birthdays))

num_experiments = 10000
successful_experiments = sum(experiment() for _ in range(num_experiments))

probability = successful_experiments / num_experiments

print(f"Approx. probability: {probability}")