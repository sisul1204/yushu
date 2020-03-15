# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/14 16:53

import threading


def worker():
    print('i am sisul')
    t = threading.current_thread()
    print(t.getName())

t = threading.current_thread()
print(t.getName())

new_t = threading.Thread(target=worker, name='sisul threading')
new_t.start()
