from numpy.random import default_rng
import time
from multiprocessing import Process
from threading import Thread

def computeLoad(rangeParam, storeArrayParam):
    for i in rangeParam:
        rng = default_rng()
        storeArrayParam[i] = max(abs(rng.uniform(size=500)))

if __name__ == '__main__':

    iterations = 100000
    storeArray = [0] * iterations
    maxProcesses = 4

    # divide in processes
    start_time = time.time()
    processes = [None] * maxProcesses

    for i in range(maxProcesses):
        begin = (iterations//maxProcesses) * i
        end = ((iterations//maxProcesses) * (i+1)) -1
        processes[i] = Process(target = computeLoad, args=(range(begin, end), storeArray))
    for i in range(maxProcesses):
        processes[i].start()
    for i in range(maxProcesses):
        processes[i].join()

    print("--- Divide in %s proceses takes %s seconds ---" % (maxProcesses, (time.time() - start_time)))

    # divide in theads
    start_time = time.time()
    threads = [None] * maxProcesses

    for i in range(maxProcesses):
        begin = (iterations//maxProcesses) * i
        end = ((iterations//maxProcesses) * (i+1)) -1
        threads[i] = Thread(target = computeLoad, args=(range(begin, end), storeArray))
    for i in range(maxProcesses):
        threads[i].start()
    for i in range(maxProcesses):
        threads[i].join()

    print("--- Divide in %s threads takes %s seconds ---" % (maxProcesses, (time.time() - start_time)))

    # serial execution
    start_time = time.time()
    computeLoad(range(iterations), storeArray)
    print("--- Serial execution takes %s seconds ---" % (time.time() - start_time))


    