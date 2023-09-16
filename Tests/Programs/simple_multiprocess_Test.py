from simple_multiprocessing import MultiThread, MultiProcess, Task
import random, time

def test_func(i: int) -> float:
    print('started:', i)

    start = time.time()
    start / i

    if random.random() < 0.5:
        while True:
            time.sleep(0.01)

    res = time.time() - start

    return res

tasks = [Task(test_func, i) for i in range(5)]

# via threading
results_via_threading = MultiThread(tasks).solve(timeout=1)

for i, r in enumerate(results_via_threading):
    print(i, type(r), r)

# if __name__ == '__main__':
    # frozenset
# via Multiproccess
results_via_multiprocess = MultiProcess(tasks).solve(timeout=1)

for i, r in enumerate(results_via_multiprocess):
    print(i, type(r), r)





def Rohan(self):
    print("Hello My Name is Rohan.")
    time.sleep(2)
    Rohan()

def Sumit(self):
    print("Hello! My Name is  Sumit.")
    time.sleep(2)
    Sumit()





task1 = [Task(Rohan, i) for i in range(5)]
task2 = [Task(Sumit, i) for i in range(5)]

# via threading
results_via_threading1 = MultiThread(task1).solve(timeout=10)
results_via_threading2 = MultiThread(task2).solve(timeout=10)

for i, r in enumerate(results_via_threading1):
    print(i, type(r), r)


# task2 = [Task(Sumit, i) for i in range(5)]
# task1 = Task(Rohan,10)
# task2 = Task(Sumit,10)
# MultiProcess(task1)
# MultiProcess(task2).solve(timeout=300)
# results_via_multiprocess1 = MultiProcess(task1)
# results_via_multiprocess2 = MultiProcess(task2)
