import time
from multiprocessing import Process, Queue
from queue import Empty


class Ball:
    def __init__(self, name, n_bounces):
        self.name = name
        self.n_bounces = n_bounces

    def __str__(self):
        return f'{self.name} ({self.n_bounces})'


def bounce(name, delay, task_queue, done_queue):
    global new_ball
    while True:
        time.sleep(delay)
        if done_queue.full():
            print(f"[{name}] done_queue is full. Process will stop.")
            break
        try:
            new_ball = task_queue.get(1, 1)
            new_ball.n_bounces -= 1
            if new_ball.n_bounces == 0:
                done_queue.put(new_ball)
            else:
                task_queue.put(new_ball)
            pass
        except Empty:
            print(f'queue.Empty exception.')
        else:
            pass
        print(f'{name} bounces the {new_ball.name} ({new_ball.n_bounces}).')


def run_processes(balls, args):
    processes = []
    task_queue = Queue()
    done_queue = Queue(len(balls))

    for ball in balls:
        task_queue.put(ball)
    for name, delay in args:
        new_proc = Process(target=bounce, args=(name, delay, task_queue, done_queue))
        new_proc.start()
        processes.append(new_proc)
    for p in processes:
        p.join()
