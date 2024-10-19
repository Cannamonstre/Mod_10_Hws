import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


file_names = [f'./file {number}.txt' for number in range(1, 5)]

#  Linear, approx 3.7 secs
"""start = time.time()

for file_name in file_names:
    read_info(file_name)

end = time.time()
print(f'Worktime with linear programming is {end - start} sec(s)')"""

#  Multiprocessing, approx 1.5 secs
if __name__ == '__main__':
    start_mp = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, file_names)
        pool.close()
        pool.join()
    end_mp = time.time()
    print(f'Worktime with multiprocessing is {end_mp - start_mp} sec(s)')
