
class Solution:
    def topKFrequent(self, words, k: int):
        d = {}
        res = []
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        tmp = list(d.items())
        tmp.sort(key=lambda x: (-x[1], x[0]))
        #print(tmp)
        for j in range(k):
            res.append(tmp[j][0])
        return res
if __name__ == "__main__":
    word=["i", "love", "leetcode", "i", "love", "coding"]
    res=Solution().topKFrequent(word,2)


from heapq import nsmallest
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = {}
        for i, w in enumerate(words):
            counts[w] = counts.get(w, 0) + 1
        return nsmallest(k, counts, lambda i: (-counts[i], i))


