# def fb(n):
#     if n<2:
#         return n
#     else:
#         return fb(n-2) + fb(n-1)

# print(fb(10))
# def Fib_recursion(n):
#     if n<2:
#         return n
#     return Fib_recursion(n-1) + Fib_recursion(n-2)

# def Fib_tail_recursion(n,res,temp):
#     if n==0:
#         return res
#     else:
#         return Fib_tail_recursion(n-1,temp,res+temp)
# def Fib_circle(n):
#     a=0
#     b=1
#     for i in range(1,n):
#         c=a+b
#         a=b
#         b=c
#     return c
# n=10
# print(Fib_recursion(n))
# print(Fib_tail_recursion(n,0,1))
# print(Fib_circle(n))
# class Node(object):
#     def __init__(self):
#         self.date = '#'
#         self.l_tree = None
#         self.r_tree = None
# class Tree(Node):
#     def create_tree(self,tree):
#         date = raw_input('->')
#         if date == '#':
#             tree = None
#         else:
#             tree.data == data
#             tree.l_tree = Node()
#             self.create_tree(tree.l_tree)
#             tree.r_tree = Node()
#             self.create_tree(tree.r_tree)
#     def print_all(self,tree):
#         if tree.data != '#'
#             print str(tree.data) + '\t'
#     def pre_tree(self,tree)
#         if tree is not None:
#             self.print_all(tree)
#             self.pre_tree(tree.l_tree)
#             self.pre_tree(tree.r_tree)
# de
# class Node(object):
#     def __init__(self,elem = -1,lchild = None,rchild = None):
#         self.lchild = lchild
#         self.rchild = rchild

# class Tree(object):
#     def __init__(self):
#         self.root = Node()
#         self.myQueue = []
#     def add_node(self,elme):
#         node = Node(elme)
#         if self.root.elme == -1:
#             self.root = node
class Node():

    def __init__(self,data):

        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)
    1 = Node('1')
    2 = Node('2')
    3 = Node('3')
    4 = Node('4')
    5 = Node('5')
    6 = Node('6')
    7 = Node('7')
    1.left = 2
    2.left = 3
    2.right = 4
    4.left = 5
    4.right = 6
    5.right = 7
def quicksort(sor):
    if len(sor) <=1:
        return sor
    i = sor[0]
    sor_a,sor_b = [], []
    for j in range(1,len(sor)):
        if sor[j] >= i:
            sor_b.append(sor[j])
        else:
            sor_a.append(sor[j])
    print sor_a,sort_b
    return quicksort(sor_a) + [i] + quicksort(sor_b)




