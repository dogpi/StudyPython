import time

print(time.perf_counter())
# print(time.process_time())
sum = 0
for i in range(100000000):
    sum+=i
print(time.perf_counter())
# print(time.process_time())