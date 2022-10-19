"""
Threading & MultiProcessing: Allows you to run in parallel and speed up your code

Process: An instance of a program (i.e. Python interpreter, one Firefox browser )
+ Advantages:
    + Takes advantage of multiple CPUs and cores
    + Separate memory space -> Memory is not shared between processess
    + Great for CPU-bound processing
    + New process is stated independently from other processes
    + Processes are interruptable/killable
    + One Global Interpreter Lock (GIL) for each process -> avoids GIL limitation
        - GIL: Lock in Python that allows only one thread at a time to execute.
            - Needed in CPython because memory management is not thread-safe
            - Avoid:
                - Use multiprocesing
                - Use a different, free-threaded Python implementation (Jython, IronPython)
                - use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy
- Disadvantages:
    - Heavyweight
    - Starting a process is slower than starting a thread
    - More memory
    - IPC (inter-process communication) is more complicated

Thread: An entity w/in a process that can be scheduled (also known as "leightweight" process)
A process can spawn multiple threads.
+ Advantages:
    + All threads within a process share the same memory
    + Leightweight
    + Starting a thread is faster than starting a process
    + Great for I/O-bound tasks
- Disadvantages:
    - Threading is limited by GIL: Only one thread at a time
    - No effect for CPU-bound tasks
    - Not interruptable/killable
    - Careful with race conditions - will easily cause bugs or crashes
        - race conditions: when 2 or more threads want to modify the same variable at the same time
"""

### [MultiProcessing]
from multiprocessing import Process
import os
from time import sleep

def square_numbers(): # define a function to call later
        sleep(1) # wait some time for learning purposes only
        print('Testing...')

processes = [] # create a list where you will store all of your processes
num_process = 4 #os.cpu_count() # define the number of processes by # of CPUs on your machine

# entry point
if __name__ == '__main__':
    # create a process
    for i in range(num_process):
        p = Process(target=square_numbers)
        processes.append(p)
    # run/start the process
    for p in processes:
        p.start()
    # wait for the process to finish
    for p in processes:
        print('Waiting for the process...')
        p.join()  # wait for a process to finish, and while waiting - you are blocking the main thread. You block the main thread until all processes are finished.

print('end main')

# # SuperFastPython.com
# # example of running a function in another process
# from time import sleep
# from multiprocessing import Process
#
# # a custom function that blocks for a moment
# def task():
#     # block for a moment
#     sleep(1)
#     # display a message
#     print('This is from another process')
#
# # entry point
# if __name__ == '__main__':
#     # create a process
#     process = Process(target=task)
#     # run the process
#     process.start()
#     # wait for the process to finish
#     print('Waiting for the process...')
#     process.join()
#


print('\n')

# ### [Threading]
# from threading import Thread
# import os
# from time import sleep
#
# def square_numbers(): # define a function to call later
#         sleep(1) # wait some time for learning purposes only
#         print('Testing...')
#
# threads = [] # create a list where you will store all of your threads
# num_threads= 10 #os.cpu_count() # define the number of threads
#
# # entry point
# if __name__ == '__main__':
#     # create a process
#     for i in range(num_threads):
#         t = Thread(target=square_numbers)
#         threads.append(t)
#     # run/start the process
#     for t in threads:
#         t.start()
#     # wait for the process to finish
#     for t in threads:
#         print('Waiting for the threaded process...')
#         t.join()  # wait for a process to finish, and while waiting - you are blocking the main thread. You block the main thread until all processes are finished.
#
# print('end main')

### [Threading]
from threading import Thread
import os
from time import sleep

print('BEGINNING THREADING...\n')
def square_numbers(): # define a function to call later
        sleep(1) # wait some time for learning purposes only
        print('Testing...')

threads = [] # create a list where you will store all of your threads
num_threads= 10 #os.cpu_count() # define the number of threads

# create a process
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# run/start the process
for t in threads:
    t.start()
# wait for the process to finish
for t in threads:
    print('Waiting for the threaded process...')
    t.join()  # wait for a process to finish, and while waiting - you are blocking the main thread. You block the main thread until all processes are finished.

print('end main')