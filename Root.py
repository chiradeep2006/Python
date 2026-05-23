class Node: def init(self, data): self.data = data self.left = None self.right = None 
root = Node(1) root.left = Node(2) root.right = Node(3) 
queue = [root] 
while queue: node = queue.pop(0) 
print(node.data, end=" ") 
 
if node.left: 
    queue.append(node.left) 
 
if node.right: 
    queue.append(node.right