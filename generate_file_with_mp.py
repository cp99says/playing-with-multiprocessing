import random
import string
import multiprocessing
import time

a = time.time()
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def write_chunk(file_path, num_lines, line_length, chunk_id):
    with open(file_path, 'a') as file:
        for _ in range(num_lines):
            random_string = generate_random_string(line_length)
            file.write(random_string + '\n')

def generate_large_file_multiprocessing(file_path, num_lines, line_length, num_processes):
    chunk_size = num_lines // num_processes
    processes = []
    for i in range(num_processes):
        process = multiprocessing.Process(target=write_chunk, args=(file_path, chunk_size, line_length, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

file_path = 'data.txt'
num_lines = 1000000  
line_length = 100  
num_processes = multiprocessing.cpu_count() 
open(file_path, 'w').close()
generate_large_file_multiprocessing(file_path, num_lines, line_length, num_processes)
b = time.time()
print("file generated")
print(b-a)