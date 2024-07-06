import random
import string
import time

a = time.time()
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_large_file(file_path, num_lines, line_length):
    with open(file_path, 'w') as file:
        for _ in range(num_lines):
            random_string = generate_random_string(line_length)
            file.write(random_string + '\n')


file_path = 'data.txt'
num_lines = 1000000  
line_length = 100 
generate_large_file(file_path, num_lines, line_length)
b = time.time()
print(b-a)
print("file generated")
