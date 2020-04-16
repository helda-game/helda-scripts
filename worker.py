
import client

import time

iteration_ctx = None

def process_iteration(iteration_count, iteration_handler):
    global iteration_ctx
    iteration_ctx = iteration_handler(iteration_count, iteration_ctx)


def main_loop(iteration_handler):
    it_cnt = 0
    while True:
        process_iteration(it_cnt, iteration_handler)
        it_cnt += 1
        time.sleep(1)

def start_worker(iteration_handler):
    client.login()
    if client.world_id:
        print("Login success!")
        main_loop(iteration_handler)

# start_worker(lambda i: print(i))
