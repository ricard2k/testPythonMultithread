# Python Threads and Processes

I was working in an intensive calculation project. And trying to divide it in threads, I've seen that python only execute one concurrent thread at the time.

Seems that the python interpreter has a Global Interpreter Lock (GIL) that protects its own execution to be multithread. It is funny, because this not isolate you to enter in a run condition, but makes the multithreading execution slower than serial execution. More info in: http://jessenoller.com/blog/2009/02/01/python-threads-and-the-global-interpreter-lock


The solution is to use the [Python's multiprocessing module](http://docs.python.org/library/multiprocessing.html)

## Testing code

The file testMultiThread.py executes the same compute load in one execution and dividing it in processes and threads, and prints the elapsed time of each of the executions:

```
rpr@RICKS-MBP testPythonMultithread % /usr/local/bin/python3 testMultithread.py
--- Divide in 4 proceses takes 1.873093843460083 seconds ---
--- Divide in 4 threads takes 6.3145458698272705 seconds ---
--- Serial execution takes 5.188245058059692 seconds ---
```