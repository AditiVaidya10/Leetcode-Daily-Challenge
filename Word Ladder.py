class Solution:
    def ladderLength(self, start: str, end: str, wordList: List[str]) -> int:
        if start==end:
            return 0
        words=set(wordList)
        if end not in words: return 0
        words.add(start)
        alphas=[chr(i) for i in range(ord('a'),ord('z')+1)]
        q = deque([(start,1)])
        vals=defaultdict(list)
        while q:
            curr,d=q.popleft()
            if curr==end: return d
            for i in range(len(curr)):
                for j in alphas:
                    new_word=curr[:i]+j+curr[i+1:]
                    if new_word in words:
                        q.append([new_word, d+1])
                        words.remove(new_word)
        return 0
