def sumOfLeftLeaves(root):
    if not root:
        return 0

    ans = 0

    if root.left:
        if not root.left.left and not root.left.right:
            ans += root.left.val
        else:
            ans += sumOfLeftLeaves(root.left)

    ans += sumOfLeftLeaves(root.right)

    return ans


print(sumOfLeftLeaves([3, 9, 20, null, null, 15, 7]))
