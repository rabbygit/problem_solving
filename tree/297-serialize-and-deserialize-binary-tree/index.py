# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        serialized = []

        def dfs(root):
            if root is None:
                serialized.append("N")
                return 
                
            serialized.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(serialized)

    def deserialize(self, data):
        self.i = 0
        nodes = data.split(",")

        def dfs():
            if nodes[self.i] == "N":
                self.i += 1
                return None

            root = TreeNode(int(nodes[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))