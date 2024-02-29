class Bird:
    def __init__(self, xType, xRate, xWing):
        self.type = xType
        self.rate = xRate
        self.wing = xWing

class BSTreeNode:
    def __init__(self, xType, xRate, xWing):
        self.bird = Bird(xType, xRate, xWing)
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, xType, xRate, xWing):
        if xType[0] == 'B' or xRate > 10:
            return  # do nothing
        newNode = BSTreeNode(xType, xRate, xWing)
        if self.root is None:
            self.root = newNode
        else:
            self._insert_helper(self.root, newNode)

    def _insert_helper(self, root, newNode):
        if newNode.bird.rate < root.bird.rate:
            if root.left is None:
                root.left = newNode
            else:
                self._insert_helper(root.left, newNode)
        else:
            if root.right is None:
                root.right = newNode
            else:
                self._insert_helper(root.right, newNode)

    def preorder(self, root, result):
        if root:
            if root.bird.wing >= 4 and root.bird.wing <= 10:
                result.append(f"({root.bird.type},{root.bird.rate},{root.bird.wing})")
            self.preorder(root.left, result)
            self.preorder(root.right, result)

    def breadth_first_traversal(self, root, result):
        if not root:
            return
        queue = [root]
        level = 1
        while queue:
            nodeCount = len(queue)
            for _ in range(nodeCount):
                node = queue.pop(0)
                if level % 2 != 0:
                    result.append(f"({node.bird.type},{node.bird.rate},{node.bird.wing})")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

    def postorder(self, root, result):
        if root:
            self.postorder(root.left, result)
            self.postorder(root.right, result)
            if root.bird.wing <= 4 and root.bird.rate > 6:
                result.append(f"({root.bird.type},{root.bird.rate},{root.bird.wing})")

def f0():
    return "He181396" 

def f1():
    bst = BSTree()
    data = [("A", 5, 9), ("E", 2, 5), ("D", 8, 6), ("F", -6, 7), ("X", 4, 5), ("Y", 6, -7)]
    for item in data:
        bst.insert(*item)
    result = []
    bst.preorder(bst.root, result)
    return " ".join(result)

def f2():
    bst = BSTree()
    data = [("C1", 9, 2), ("D", 6, 2), ("F", 2, 3), ("Z", 8, 1), ("H", 1, 7), ("I", 3, 9),
            ("Z1", 7, 1), ("J", 5, 5), ("K", 4, 1)]
    for item in data:
        bst.insert(*item)
    result = []
    bst.preorder(bst.root, result)
    return " ".join(result)

def f3():
    bst = BSTree()
    data = [("C", 8, 2), ("D", 6, 1), ("F", 2, 3), ("H", 1, 7), ("I", 3, 9), ("J", 5, 5),
            ("K", 4, 6), ("G", 7, 8), ("E", 9, 4)]
    for item in data:
        bst.insert(*item)
    result = []
    bst.breadth_first_traversal(bst.root, result)
    return " ".join(result)

def f4():
    bst = BSTree()
    data = [("C", 8, 2), ("D", 6, 1), ("F", 2, 3), ("H", 1, 7), ("I", 3, 9), ("J", 5, 8),
            ("K", 4, 6), ("G", 7, 3), ("E", 9, 4)]
    for item in data:
        bst.insert(*item)
    result = []
    bst.postorder(bst.root, result)
    return " ".join(result)
def main():
    while True:
        print("\nMenu:")
        print("1. Run f0()")
        print("2. Run f1()")
        print("3. Run f2()")
        print("4. Run f3()")
        print("5. Run f4()")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("Output of f0():", f0())
        elif choice == '2':
            print("Output of f1():", f1())
        elif choice == '3':
            print("Output of f2():", f2())
        elif choice == '4':
            print("Output of f3():", f3())
        elif choice == '5':
            print("Output of f4():", f4())
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
