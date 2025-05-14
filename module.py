# def welcome():
#     print("hello world")

# # welcome() #print twice if call through import
# print(__name__)
# if __name__ == "__main__":
#     welcome()
import threading

import time
def fun(seconds):
    print(f"program run for {seconds}")
    time.sleep(seconds)
threading.Thread(target=fun,args=(4,))
threading.Thread(target=fun,args=(2,))
# fun(4)
# fun(3)
# fun(1)