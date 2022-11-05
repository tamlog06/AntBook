class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data):
        self.root = None
        for x in data:
            self.insert(x)

    def insert(self, x):
        n = self.root
        # 初期時点ではxを値とするデータクラスでrootを初期化する
        if self.root is None:
            self.root = Node(x)
            return

        while True:
            # xがnの値より小さい場合
            if x < n.data:
                if n.left is None:
                    n.left = Node(x)
                    return
                n = n.left
            # xがnの値より大きい場合
            elif x > n.data:
                if n.right is None:
                    n.right = Node(x)
                    return
                n = n.right
            # xがnの値と等しい場合は何もしない
            else:
                return

    def find(self, x):
        n = self.root
        while n is not None:
            if x < n.data:
                n = n.left
            elif x > n.data:
                n = n.right
            else:
                return True

        return False

    def remove(self, x):
        n = self.root
        while n is not None:
            if x < n.data:
                n = n.left
            elif x > n.data:
                n = n.right
            else:
                break

        if n is None:
            return False

        node = n

        if n.left is None: 
            n = n.right
        elif n.left.right is None:
            n = n.left
        else:
            n = n.left
            while n.right is not None:
                parent = n
                n = n.right

            parent.right = n.left
            node.data = n.data
        
        return True

if __name__ == '__main__':
    # 実際には偏りが生じる可能性もあるので、基本的にはbisectを使えば良く、木にして扱う必要はない
    import random
    iarray_A = list(range(20))
    random.shuffle(iarray_A)
    print(iarray_A)

    tree = BinarySearchTree(iarray_A)
    print(tree.find(10))
    print(tree.find(20))
    print(tree.remove(5))
    print(tree.find(5))
    print(tree.insert(25))
    print(tree.find(25))

