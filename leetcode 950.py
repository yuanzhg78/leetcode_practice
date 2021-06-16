from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort()#small to large
        i=len(deck)-2
        array=deque()
        array.append(deck[-1])
        while (i>=0):
            t=array.pop()
            array.appendleft(t)
            array.appendleft(deck[i])
            i-=1

        return list(array)



if __name__ == "__main__":
    #root = [3,9,20,None,None,15,7]

    deck= [17,13,11,2,3,5,7]
    res = Solution().deckRevealedIncreasing(deck)



class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort(reverse=True)
        l = list()
        for i in deck:
            if not l:
                l.append(i)
            else:
                l.insert(0, l.pop())
                l.insert(0, i)
        return l
