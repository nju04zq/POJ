import sys
import time
import random
import traceback
import multiprocessing

random.seed()

_RANDINT_MIN_ = 0
_RANDINT_MAX_ = 100

def randint(min_int=None, max_int=None):
    if min_int is None:
        min_int = _RANDINT_MIN_
    if max_int is None:
        max_int = _RANDINT_MAX_
    return random.randint(min_int, max_int)

def randint_array(min_int=None, max_int=None, size=None):
    if min_int is None:
        min_int = _RANDINT_MIN_
    if max_int is None:
        max_int = _RANDINT_MAX_
    if size is None:
        size = randint(min_int=0, max_int=63)
    array = [randint(min_int, max_int) for i in xrange(size)]
    return array

def randint_sorted_array(min_int=None, max_int=None, size=None, reverse=False):
    array = randint_array(min_int, max_int, size)
    array.sort(reverse=reverse)
    return array

class ListNode(object):
    def __init__(self, data=0):
        self.data = data
        self.next = None

def generate_list(size=None):
    if size is None:
        size = randint(min_int=1, max_int=10)
    head, prev = None, None
    for i in xrange(size):
        node = ListNode()
        if head is None:
            head = node
        if prev is not None:
            prev.next = node
        prev = node
    return head

def append_list(head, node):
    if head is None:
        head = node
        return
    p = head
    while p is not None:
        prev = p
        p = p.next
    prev.next = node

def remove_list_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    p = head
    while p.next is not None:
        prev = p
        p = p.next
    prev.next = None
    return head

def get_list_tail(head):
    if head is None:
        return None
    p = head
    while p is not None:
        prev = p
        p = p.next
    return prev

def get_list_size(head):
    p, size = head, 0
    while p is not None:
        size += 1
        p = p.next
    return size

def dump_list(head):
    if head is None:
        return "None"
    p, s = head, ""
    while p is not None:
        if p.next is not None:
            s += "{0} -> ".format(id(p))
        else:
            s += "{0}".format(id(p))
        p = p.next
    return s

def copy_list(a):
    node_map = {}
    a1 = None
    p, prev = a, None
    while p is not None:
        if id(p) in node_map:
            prev.next = node_map[id(p)]
            break
        node = ListNode(p.data)
        if a1 is None:
            a1 = node
        if prev is not None:
            prev.next = node
        node_map[id(p)] = node
        prev = node
        p = p.next
    return a1

def dump_loop_list(a):
    node_set = set()
    p, s = a, ""
    while p is not None:
        if id(p) in node_set:
            s += " -> {0}".format(id(p))
            break
        node_set.add(id(p)) 
        if p is a:
            s += str(id(p))
        else:
            s += " -> {0}".format(id(p))
        p = p.next
    return s

def copy_list_pair(a, b):
    node_map = {}
    a1, b1 = None, None
    p, prev = a, None
    while p is not None:
        node = ListNode(p.data)
        node_map[id(p)] = node
        if a1 is None:
            a1 = node
        if prev is not None:
            prev.next = node
        prev = node
        p = p.next
    p, prev = b, None
    while p is not None:
        if id(p) in node_map:
            node = node_map[id(p)]
        else:
            node = ListNode(p.data)
        if b1 is None:
            b1 = node
        if prev is not None:
            prev.next = node
        prev = node
        p = p.next
    return a1, b1

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
            env["err"] = traceback.format_exc()
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
