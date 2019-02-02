from memory_profiler import profile


# Profile не работает с генератором "yeld"

@profile
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b


fib(1000)


# Line #    Mem usage    Increment   Line Contents
# ================================================
#      6     13.3 MiB     13.3 MiB   @profile
#      7                             def fib(n):
#      8     13.3 MiB      0.0 MiB       a, b = 0, 1
#      9     13.3 MiB      0.0 MiB       while a < n:
#     10     13.3 MiB      0.0 MiB           print(a)
#     11     13.3 MiB      0.0 MiB           a, b = b, a + b