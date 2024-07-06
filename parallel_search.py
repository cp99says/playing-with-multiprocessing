import multiprocessing

def load_dataset(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

def divide_chunks(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def search_chunk(chunk, query, start_index):
    results = []
    query = query.lower()
    for i, item in enumerate(chunk):
        if query in item.lower():
            results.append((start_index + i, item))
    return results

def parallel_search(data, query, num_processes):
    chunk_size = len(data) // num_processes
    chunks = list(divide_chunks(data, chunk_size))

    with multiprocessing.Pool(num_processes) as pool:
        results = pool.starmap(search_chunk, [(chunk, query, i * chunk_size) for i, chunk in enumerate(chunks)])

    return [item for sublist in results for item in sublist]

file_path = 'data.txt'
query = 'cheta'
num_processes = multiprocessing.cpu_count()

data = load_dataset(file_path)
results = parallel_search(data, query, num_processes)

for line_num, line in results:
    print(f"Line {line_num}: {line}")
