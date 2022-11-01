'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/11/1 9:28 
前序遍历：根左右
中序遍历：左根右
后序遍历：左右根
'''


# 二叉搜索树python3实现
class BST:
    def __init__(self, value):
        # 每一个节点都可以看作是一个小的二叉树，都有左子树和右子树，只不过有的是空有的不是空
        self.value = value
        self.left = None
        self.right = None


def previousTraversal(tree, array=[]):
    if tree is None:
        return []
    else:
        # 前序遍历：先根再左最后右
        array.append(tree.value)
        previousTraversal(tree.left, array)
        previousTraversal(tree.right, array)
    return array




def middleTraversal(tree, array=[]):
    if tree is None:
        return []
    else:
        # 中序遍历：先左再根最后右
        middleTraversal(tree.left, array)
        array.append(tree.value)
        middleTraversal(tree.right, array)
    return array


def postTraversal(tree, array=[]):
    if tree is None:
        return []
    else:
        # 后序遍历：先左再右最后根
        postTraversal(tree.left, array)
        postTraversal(tree.right, array)
        array.append(tree.value)
    return array


# 先从根节点开始
bst = BST(20)
# 再到根节点的左子树和右子树
# 左子树
bst.left = BST(14)
bst.left.left = BST(9)
bst.left.right = BST(19)
bst.left.right.left = BST(18)
# 右子树
bst.right = BST(23)
bst.right.left = BST(21)
bst.right.right = BST(27)
bst.right.right.left = BST(24)
bst.right.right.right = BST(30)
print(u'前序遍历：')
print(previousTraversal(bst, array=[]))
print(u'中序遍历：')
print(middleTraversal(bst, array=[]))
print(u'后序遍历：')
print(postTraversal(bst, array=[]))