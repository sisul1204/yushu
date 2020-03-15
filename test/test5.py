# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/15 10:53
import threading
import time


class A:
    b = 1


my_obj = A()

def worker():
    my_obj.b = 2

new_t = threading.Thread(target=worker, name='sisul_thread')
new_t.start()
time.sleep(1)
print(my_obj.b)
