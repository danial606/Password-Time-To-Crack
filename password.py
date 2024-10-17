import math

def calculate_password_strength(password):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_chars = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~\""

    char_set_size = 0
    if any(char in lowercase for char in password):
        char_set_size += 26
    if any(char in uppercase for char in password):
        char_set_size += 26
    if any(char in numbers for char in password):
        char_set_size += 10
    if any(char in special_chars for char in password):
        char_set_size += 32
    
    password_length = len(password)
    total_combinations = char_set_size ** password_length
    guesses_per_second = 10**10
    time_to_crack_seconds = total_combinations / guesses_per_second
    time_to_crack_readable = time_to_crack(time_to_crack_seconds)

    return total_combinations, time_to_crack_seconds, time_to_crack_readable

def time_to_crack(seconds):
    time = [
        ('year', 60 * 60 * 24 * 365),
        ('day', 60 * 60 * 24),
        ('hour', 60 * 60),
        ('minute', 60),
        ('second', 1)
    ]
    
    result = []
    for time_name, time_seconds in time:
        if seconds >= time_seconds:
            time_value, seconds = divmod(seconds, time_seconds)
            result.append(f"{int(time_value)} {time_name}{'s' if time_value > 1 else ''}")

    return ', '.join(result)

password = input("Enter password:")
combinations, time_seconds, time_readable = calculate_password_strength(password)

print(f"Total Combinations: {combinations}")
print(f"Time to Crack (seconds): {time_seconds}")
print(f"Time to Crack (readable): {time_readable}")
