"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        visited = {}
        Q = deque([node])
        visited[node] = Node(node.val, [])
        while Q:
            currNode = Q.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    Q.append(neighbor)
                visited[currNode].neighbors.append(visited[neighbor])

        return visited[node]
