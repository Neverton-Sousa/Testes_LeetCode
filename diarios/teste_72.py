class Solution:
    def __init__(self):
        self.sum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            root.val += self.sum
            self.sum = root.val
            self.bstToGst(root.left)
        return root