#закодировать строку по алгоритму Хаффмана
from collections import Counter, deque

class Node:
   def __init__(self, value=None, left=None, right=None):
       self.value = value
       self.left = left
       self.right = right

   def __repr__(self):
       return f'Node[{self.value}]'

class Tree:
    def __init__(self):
        self.root = None


    def new_node(self, value):
       """функция для добавления узла в дерево"""
       return Node(0, None, None)
def haff(string):
    """функция объеденения двух меннее встречающихся символов"""
    count = Counter(string)
    deque_count = deque(count.most_common())
    while len(deque_count) > 1:
        w = deque_count[-2][-1] + deque_count[-1][-1]
        #Node(value=w, left=deque_count.pop()[-2], right=deque_count.pop()[-2])
        deque_count.append((Node(value=w, left=deque_count.pop()[-2], right=deque_count.pop()[-2]), w))
        deque_count = sorted(deque_count, reverse=True, key=lambda item: item[1])
        print(f'{deque_count}')
    return deque_count[0]

    #print(w)
    #print(deque_count)
string = 'beepboopbeer'#input('введите строку для кодирования :')
print(haff(string))



