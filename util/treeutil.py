class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_trees_from(nums):
    if len(nums) == 0:
        return [None]
    elif len(nums) == 1:
        return [TreeNode(nums[0])]
    trees = []
    for i in xrange(len(nums)):
        res1 = make_trees_from(nums[:i])
        res2 = make_trees_from(nums[i+1:])
        for root1 in res1:
            for root2 in res2:
                root = TreeNode(nums[i])
                root.left, root.right = root1, root2
                trees.append(root)
    return trees

def make_trees_with(n):
    nums = [i for i in xrange(1, n+1)]
    return make_trees_from(nums)

def make_balanced_tree_from(nums):
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return TreeNode(nums[0])
    mid = (len(nums)-1)/2
    root = TreeNode(nums[mid])
    root.left = make_balanced_tree_from(nums[:mid])
    root.right = make_balanced_tree_from(nums[mid+1:])
    return root

def make_balanced_tree(i):
    nums = [i for i in xrange(1, i+1)]
    return make_balanced_tree_from(nums)

def make_trees():
    # catalan number, c(13) = 742900, c(14) = 2674440
    maxN = 4
    data = [None]
    for i in xrange(1, maxN+1):
        data += make_trees_with(i)
    for i in xrange(maxN+1, 100):
        data.append(make_balanced_tree(i))
    return data

def dump_tree(root):
    if root == None:
        print "Empty tree"
        return
    vals, nodes = [], [root]
    while len(nodes) > 0:
        cnt = len(nodes)
        for i in xrange(cnt):
            if nodes[i] is None:
                vals.append("#")
            else:
                vals.append(str(nodes[i].val))
                nodes.append(nodes[i].left)
                nodes.append(nodes[i].right)
        nodes = nodes[cnt:]
    for i in xrange(len(vals)-1, -1, -1):
        if vals[i] != "#":
            break
    vals = vals[:i+1]
    print vals

if __name__ == "__main__":
    roots = make_trees()
    for root in roots:
        dump_tree(root)
