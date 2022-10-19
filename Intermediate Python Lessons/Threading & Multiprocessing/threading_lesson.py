"""
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

- Create & Start multiple threads
- Sharing data between threads
- Using locks to prevent race conditions
- Daemon process
- Using queue for thread safe data exchanges: Excellent for thread safe and process safe data exchanges, data processing in multi threaded or multiprocessing environments
"""

### [Threading] Create & Start multiple threads
from threading import Thread

print('BEGINNING BASIC THREADING...\n')

def square_numbers(): # define a function to call later
        for i in range(100):
            i * i
            print('Testing...')

if __name__ == "__name__":
    threads = [] # create a list where you will store all of your threads
    num_threads= 10 # define the number of threads

    # create a process
    for i in range(num_threads):
        i = Thread(target=square_numbers) # call function
        threads.append(threads)

    # run/start the process
    for thread in threads:
        thread.start()
    # wait for the process to finish
    for thread in threads:
        print('Waiting for the threaded process...')
        thread.join()  # wait for a process to finish, and while waiting - you are blocking the main thread. You block the main thread until all processes are finished.

    print('end main')

print('\n')


### [Threading] Sharing Data Between Threads
# Threads live in the same memory space; they have access to the same data
from threading import Thread
import time

print('BEGINNING SHARING DATA THREADING...\n')

database_value = 0 # define a global value

def increase():
    global database_value # call global value to be modified
    local_copy = database_value # grabs database value and stores it in a local copy
    # processing
    local_copy += 1 # increments local copy
    time.sleep(0.1) # program intelligently switches to other threads and uses the waiting time | latent race condition; two thrads are attempting to modify the same value around here
    database_value = local_copy

if __name__ == "__name__":
    print('start value', database_value)

    # create 2 threads
    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)

    #start both threads
    thread1.start() # grabs database value and stores it in a local copy
    thread2.start() # grabs database value and stores it in a local copy; same value as above

    # wait for the threads to complete
    thread1.join()
    thread2.join()

    print('end value', database_value)

    print('end main')

print('\n')



### [Threading] Sharing Data Between Threads w/o Race Conditions
# Threads live in the same memory space; they have access to the same data
from threading import Thread, Lock

print('BEGINNING SHARING DATA THREADING...\n')

database_valueA = 0 # define a global value

def increaseA(lock):
    global database_valueA # call global value to be modified

    lock.acquire() # prevents another thread from accessing the same code part at the same time
    local_copyA = database_valueA
    # processing
    local_copyA += 1
    time.sleep(0.1) # latent race condition; two threads are attempting to modify the same value around here
    database_valueA = local_copyA
    lock.release() # releases lock

if __name__ == "__name__":
    lock = Lock()
    print('start value', database_valueA)

    # create 2 threads
    thread1a = Thread(target=increaseA, args=(lock,)) # passes argument as a tuple
    thread2a = Thread(target=increaseA, args=(lock,))

    #start both threads
    thread1a.start()
    thread2a.start()

    # wait for the threads to complete
    thread1a.join()
    thread2a.join()

    print('end value', database_valueA)

    print('end main')

print('\n')



### [Threading] Sharing Data Between Threads w/o Race Conditions| Recommended way to use Locks: Context Manager Locking
# Threads live in the same memory space; they have access to the same data
from threading import Thread, Lock
import time

print('BEGINNING SHARING DATA THREADING...\n')

database_valueB = 0 # define a global value

def increaseA(lockB):
    global database_valueB # call global value to be modified

    with lockB:# prevents another thread from accessing the same code part at the same time | Context Manager Locking
        local_copyB = database_valueB
        # processing
        local_copyB += 1
        time.sleep(0.1) # latent race condition; two threads are attempting to modify the same value around here
        database_valueA = local_copyB
        lockB.release() # releases lock

if __name__ == "__name__":
    lockB = Lock()
    print('start value', database_valueA)

    # create 2 threads
    thread1b = Thread(target=increaseA, args=(lockB,)) # passes argument as a tuple
    thread2b = Thread(target=increaseA, args=(lockB,))

    #start both threads
    thread1b.start()
    thread2b.start()

    # wait for the threads to complete
    thread1b.join()
    thread2b.join()

    print('end value', database_valueB)

    print('end main')

print('\n')



### [Queue Threading] Using queue for thread safe data exchanges
# linear data structure that follows the First In First Out (FIFO) principle
# i.e. a queue of customers that came first; first customer to arrive gets served first

# Daemon thread is a background thread that will die when the main thread dies

from threading import Thread, Lock, current_thread
from queue import Queue
import time

print('BEGINNING QUEUE DATA THREADING...\n')

def worker(q, lockC):
    while True: # creates an infinite loop
        value = q.get()

        # processing...
        with lockC:
            print(f"in {current_thread().name} got {value}")
        q.task_done()

if __name__ == "__name__":
    q = Queue()  # create a queue object

    num_threadsC = 10

    for i in range(num_threadsC):
        threadC = Thread(target=worker, args=(q,)) # calling a tuple arguement function
        threadC.daemon = True # create a daemon thread
        threadC.start

    for i in range(1,21): # fill queue with elements
        q.put(i)

    q.join()

    # q.put(1)
    # q.put(2)
    # q.put(3)

    # # 3 2 1 --->
    # first = q.get()
    # print(first) # return the first element
    #
    # q.empty() # check if queue is empty
    #
    # q.task_done() # tells queue task is finished
    # q.join() # blocks other code until all items in queue have been fetched & processed




    print('end main')

print('\n')