import random

letters = list('abcdefghijklmnopqrstuvwxyz')
vowels = list('aeiou')
consonants = [l for l in letters if l not in vowels]

def experiment():
    draw = random.sample(letters, 2)

    return (draw[0] in vowels and draw[1] in consonants) or \
           (draw[0] in consonants and draw[1] in vowels)

num_experiments = 10000
successful_experiments = sum(experiment() for _ in range(num_experiments))

probability = successful_experiments / num_experiments

print(f"Approx. probability: {probability}")



