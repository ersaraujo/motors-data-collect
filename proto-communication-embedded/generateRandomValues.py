import random
import numpy as np

def generate_random_values_with_seed(start, end, count, seed):
    random.seed(seed)
    random_values = [round(random.uniform(start, end), 1) for _ in range(count)]
    return random_values

def load_pwm_values(file):
    pwms = np.loadtxt(file)
    return pwms

if __name__ == "__main__":
    start_range = -25
    end_range = 25
    number_of_values = 49
    seed_value = 42  # You can choose any integer as the seed
    
    random_values = generate_random_values_with_seed(start_range, end_range, number_of_values, seed_value)
    np.savetxt(f'random_pwm_values_with_seed_{seed_value}.txt', random_values)
    pwms = load_pwm_values(f'random_pwm_values_with_seed_{seed_value}.txt')
    print(pwms)
