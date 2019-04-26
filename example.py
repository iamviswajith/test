def sort_n_square(arr):
    n = len(arr)

    for k in range(n):
        if arr[k]>=0:
            break
    i = k-1
    j = k
    index = 0

    result = [None] * n

    while i>=0 and j<n:
        if arr[i]**2 < arr[j]**2:
            result[index] = arr[i]**2
            i-=1
        else:
            result[index] = arr[j]**2
            j+=1
        index+=1

    while i>=0:
        result[index] = arr[i]**2
        index += 1
        i-=1

    while j<n:
        result[index] = arr[j]**2
        index += 1
        j+=1
    print(result)




arr = [ -9 , -2 , 0 , 2 , 4  ]

sort_n_square(arr)


# class Node:
#
#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# # Function to print reverse level order traversal
# def reverseLevelOrder(root):
#     h = height(root)
#     for i in reversed(range(1, h+1)):
#         printGivenLevel(root,i)
#
# # Print nodes at a given level
# def printGivenLevel(root, level):
#
#     if root is None:
#         return
#     if level ==1 :
#         print root.data,
#
#     elif level>1:
#         printGivenLevel(root.right, level-1)
#         printGivenLevel(root.left, level-1)
#
# # Compute the height of a tree-- the number of
# # nodes along the longest path from the root node
# # down to the farthest leaf node
# def height(node):
#     if node is None:
#         return 0
#     else:
#
#         # Compute the height of each subtree
#         lheight = height(node.left)
#         rheight = height(node.right)
#
#         # Use the larger one
#         if lheight > rheight :
#             return lheight + 1
#         else:
#             return rheight + 1
#
#
# root = Node(1)
# root.left      = Node(2)
# root.right     = Node(3)
# root.right.left  = Node(6)
# root.left.right  = Node(5)
# root.left.left  = Node(4)
#
# reverseLevelOrder(root)


