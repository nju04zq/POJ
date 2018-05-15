import sys
import time
import traceback
import multiprocessing

def runtest_api(test_data_list, lock, env, passed, left):
    while True:
        lock.acquire()
        if left.value == 0 or "err" in env:
            lock.release()
            break
        left.value -= 1
        data = test_data_list.pop()
        lock.release()
        try:
            if isinstance(data, tuple):
                rc, err = env["api"](*data)
            else:
                rc, err = env["api"](data)
        except:
            env["exception"] = True
            err = "\n" + "*"*50 + "\n"
            err += "Fail on {0}\n".format(data) + traceback.format_exc()
            env["err"] = err
            break

        if rc == True:
            with passed.get_lock():
                passed.value += 1
        else:
            env["err"] = err
            break

def create_runtest_plist(test_data_list, lock, env, passed, left):
    plist = []
    RUN_PARALLEL_PROC_CNT = 2
    for i in xrange(RUN_PARALLEL_PROC_CNT):
        p = multiprocessing.Process(target=runtest_api,
                                    args=(test_data_list,lock,env,passed,left))
        plist.append(p)
    return plist

def start_runtest_plist(plist):
    for p in plist:
        p.start()

def join_runtest_plist(plist):
    for p in plist:
        p.join()

def clear_last_msg(last_msg):
    msg_len = len(last_msg)
    sys.stdout.write("\r" + " "*msg_len + "\r")
    sys.stdout.flush()

def run_test_in_parallel(run_single_test_api, test_data_list):
    test_case_size = len(test_data_list)
    manager = multiprocessing.Manager()
    env = manager.dict()
    env["api"] = run_single_test_api
    test_data_list = manager.list(test_data_list)
    passed = multiprocessing.Value("i", 0)
    left = multiprocessing.Value("i", test_case_size)
    lock = multiprocessing.Lock()
    plist = create_runtest_plist(test_data_list, lock, env, passed, left)
    start_runtest_plist(plist)
    while True:
        last_msg = "\rRunning test, {0}/{1}".format(\
                   passed.value, test_case_size)
        sys.stdout.write(last_msg)
        sys.stdout.flush()
        if left.value == 0 or "err" in env:
            break
        time.sleep(0.1)
    clear_last_msg(last_msg)
    join_runtest_plist(plist)
    if "exception" in env:
        raise Exception(env["err"])
    elif "err" in env:
        rc = False
        err = env["err"]
    else:
        rc = True
        err = ""
    return rc, passed.value, test_case_size, err
