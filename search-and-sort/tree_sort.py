from random import randint

class Node():
    def __init__(self, key):
        # This is the value of the node
        self.key = key
        # The node's children
        # Left node should be lower, right node bigger than the key
        self.left, self.right = None, None

# Function to iteratively search the tree until the right place for a key is found
def insert_key(root, key):

    # If this node is empty, create a node for it
    if root == None:
        root = Node(key)
        return root

    # Otherwise, look down the tree
    # For a smaller or equal element than the node value, look left
    if key <= root.key:
        root.left = insert_key(root.left, key)
    # For larger elements look right
    else:
        root.right = insert_key(root.right, key)

    return root
    
# Function to create the binary search tree
def create_tree(array):
    global root
    # Set the first element of the list as the root of the tree
    root = Node(array[0])
    del array[0]
    for element in array:
        root = insert_key(root, element)

# Then add the values from the tree into an array
def convert_tree_to_array(root):
    if root != None:
        # Go left until no child node exists
        convert_tree_to_array(root.left)
        # Append the value of the left-most node to the array
        sorted_array.append(root.key)
        # Then move right one node and repeat
        convert_tree_to_array(root.right)


unsorted_array = []
sorted_array = []
# Create the unsorted array
for i in range(10):
    unsorted_array.append(randint(1, 100))
print(unsorted_array)
# Create the tree
create_tree(unsorted_array)
# Convert the tree into an array
convert_tree_to_array(root)
# Print the array
print(sorted_array)