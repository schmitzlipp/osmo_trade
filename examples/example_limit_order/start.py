from example_limit_strategy import foo
import time
import multiprocessing
import sys

if __name__ == '__main__':  
    while 1:
        try:
            p = multiprocessing.Process(target=foo, name="foo")
            p.start()
            time.sleep(360)
            p.terminate()
            p.join()
            print('Restart in...')
            for i in range(10,0,-1):
                print(i)
                time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)