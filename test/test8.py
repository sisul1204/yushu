# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/15 11:51
import threading
import time

from werkzeug.local import LocalStack

my_stack = LocalStack()
my_stack.push(1)

print('in main thread after push, value is: '+ str(my_stack.top))

def worker():
    print('in new thread before push, value is: '+str(my_stack.top))
    my_stack.push(2)
    print('in new thread after push, value is: '+str(my_stack.top))

new_t = threading.Thread(target=worker, name='sisul_thread')
new_t.start()
time.sleep(1)
print('finally, in main thread value is: '+str(my_stack.top))