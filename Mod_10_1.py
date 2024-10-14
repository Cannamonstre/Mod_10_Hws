import threading
import time


def write_words(count_word, name_file):
    with open(name_file, 'w+', encoding='UTF-8') as file:  # Creating a non-existing files with 'w+'
        for i in range(1, count_word + 1):
            word = f'Some word #{i}\n'
            file.write(word)
            time.sleep(0.1)
    print(f'File {name_file} writing completed.')


time_start = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = time.time()
print(f'No threads worktime is {time_end - time_start} sec(s)')  # about 34.18 secs

time_start_thread = time.time()

t1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
t2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
t3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
t4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

time_end_thread = time.time()
print(f'With threads worktime is {time_end_thread - time_start_thread} sec(s)')  # about 20.1 secs
