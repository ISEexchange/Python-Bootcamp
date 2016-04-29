
# def my_gen(in_num):
#     print 'started'
#     a = 0
#     while a < in_num+10:
#         print a, in_num
#         yield a
#         a += in_num

# b = my_gen(20)
# # print b.next()
# print 'a:', b.send(None)
# print 'b:', b.send(26)
# print 'c:', b.next()

# print type(b)

# print b.next()
# print b.next()
# print b.next()
# print b.next()
# print b.next()

























import threading
import time


# Define a function for the thread
def print_time(threadName, delay):
    count = 0
    while count < 2:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))

new_thread_1 = threading.Thread(target=print_time, args=("Thread-1", 2))
new_thread_2 = threading.Thread(target=print_time, args=("Thread-2", 4))

new_thread_1.start()
new_thread_2.start()

# Wait for all of the threads to complete
while threading.active_count() > 1:
    pass

print 'All done'
