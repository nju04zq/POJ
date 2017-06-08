import sys
from util import ListNode, generate_list, append_list, remove_list_tail,\
                 dump_list, get_list_tail, copy_list_pair, copy_list,\
                 dump_loop_list

a = generate_list(5)
print dump_list(a)
print dump_loop_list(a)
a_tail = get_list_tail(a)
a_tail.next = a.next.next
print dump_loop_list(a)
b = copy_list(a)
print dump_loop_list(b)
