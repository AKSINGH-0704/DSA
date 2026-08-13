class Node:
    def __init__(self, char=None):
        self.lchar = char
        self.rchar = char
        self.prefix = 1 if char else 0
        self.suffix = 1 if char else 0
        self.max_len = 1 if char else 0
        self.size = 1 if char else 0

class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.tree = [None] * (4 * self.n)
        self.build(s, 0, 0, self.n - 1)

    def merge(self, left, right):
        if not left: return right
        if not right: return left
        
        parent = Node()
        parent.size = left.size + right.size
        parent.lchar = left.lchar
        parent.rchar = right.rchar
        
        parent.prefix = left.prefix
        if left.prefix == left.size and left.lchar == right.lchar:
            parent.prefix += right.prefix
            
        parent.suffix = right.suffix
        if right.suffix == right.size and right.rchar == left.rchar:
            parent.suffix += left.suffix
            
        parent.max_len = max(left.max_len, right.max_len)
        if left.rchar == right.lchar:
            parent.max_len = max(parent.max_len, left.suffix + right.prefix)
            
        parent.max_len = max(parent.max_len, parent.prefix, parent.suffix)
        return parent

    def build(self, s, node, start, end):
        if start == end:
            self.tree[node] = Node(s[start])
            return
        mid = (start + end) // 2
        self.build(s, 2 * node + 1, start, mid)
        self.build(s, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, node, start, end, idx, char):
        if start == end:
            self.tree[node] = Node(char)
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node + 1, start, mid, idx, char)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, char)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        st = SegmentTree(s)
        ans = []
        for i in range(len(queryIndices)):
            st.update(0, 0, st.n - 1, queryIndices[i], queryCharacters[i])
            ans.append(st.tree[0].max_len)
        return ans
