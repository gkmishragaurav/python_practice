# single_threaded
import time
from threading import Thread

COUNT = 60000000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start)

# multi_threaded

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//3,))
t2 = Thread(target=countdown, args=(COUNT//3,))
t3 = Thread(target=countdown, args=(COUNT//3,))

start = time.time()
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
end = time.time()

print('Time taken in seconds -', end - start)