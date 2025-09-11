class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

node1 = TreeNode('B')
node2 = TreeNode('C')
root_node = TreeNode('A', left=node1, right=node2)

