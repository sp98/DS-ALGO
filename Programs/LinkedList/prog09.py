"""
Find sum of two linked list of positive digits
l1  3 -> 4 -> 5
l2  2 -> 5 -> 9 -> 8
result = 543 + 8952
"""

from singlyLL import SinglyLL, Node

def add_two_numbers(l1, l2, l3):
    """ add l1 and l2 linkedlist into l3 linkedlist"""
    carry = 0
    prev = None

    while l1 is not None or l2 is not None:
        l1_data = 0 if l1 is None else l1.data
        l2_data = 0 if l2 is None else l2.data

        sum = carry + l1_data + l2_data
        carry = 0 if sum <10 else 1
        sum = sum if sum <10 else sum%10
        if l3 is None:
            l3 = Node(sum) 
        else:
            prev.append(sum)

        prev = l3.next
           
     
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    if carry < 0:
        l3.append(carry)

    print(l3.display())
            
if __name__ == '__main__':
    l1 = SinglyLL()
    l1.append(3)
    l1.append(4)
    l1.append(5)
    print(l1.display())

    l2 = SinglyLL()
    l2.append(2)
    l2.append(5)
    l2.append(9)
    l2.append(8)
    print(l2.display())
  
    l3 = SinglyLL()
    add_two_numbers(l1.head, l2.head, l3.head)
