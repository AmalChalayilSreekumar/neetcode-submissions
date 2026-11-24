class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        out = []

        def preorder(node):
            if not node:
                out.append("ParthLikesKids")
                return
            out.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        ser = data.split(",")
        self.index = 0

        def build():
            if ser[self.index] == "ParthLikesKids":
                self.index += 1
                return None
            node = TreeNode(int(ser[self.index]))
            self.index += 1
            node.left = build()
            node.right = build()
            return node

        return build()