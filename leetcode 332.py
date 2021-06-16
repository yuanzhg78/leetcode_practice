#dfs 用栈
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dict = {}
        #create a dict 构建一个dict存上每个src对应的所有dst（用一个list存储）
        for src, dst in tickets:
            if src in dict:
                dict[src].append(dst)
            else:
                dict[src] = [dst]
        # 因为有重复的行程，所以用了嵌套的哈希表存行程，嵌套的map会自动按字典序排序。
        # 用迭代的dfs一直搜，不断删除访问过的边，直到从某个点出发再没有其他行程了，才将这个点加入ans数组中，并将其充栈弹出。


        for src in dict.keys():
            # 对每一个src对应的list进行排序（反向排序）保证cost小的在list最后面，可以提前pop，cost大的在里面（题目的要求）
            dict[src].sort(reverse = True)
        stack = ['JFK']#出发点是JFK
        res = []#记录最后的结果
        while len(stack) > 0:
            src_elem = stack[-1]#把stack的最后一个当成src，找下一个dist
            if src_elem in dict and len(dict[src_elem]) > 0:
                stack.append(dict[src_elem].pop()) #弹出dist，加到stack中 #dfs
            else:
                res.append(stack.pop()) #这个应该是最后的目的地 没有从该点出发的行程了，弹出，加入结果
        return res[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        # Create a graph for each airport and keep list of airport reachable from it
        for src, dst in tickets:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]

        for src in graph.keys():
            graph[src].sort(reverse=True)
            # Sort children list in descending order so that we can pop last element
            # instead of pop out first element which is costly operation（昂贵的操作）
        stack = []
        res = []
        stack.append("JFK")
        # Start with JFK as starting airport and keep adding the next child to traverse
        # for the last airport at the top of the stack. If we reach to an airport from where
        # we can't go further then add it to the result. This airport should be the last to go
        # since we can't go anywhere from here. That's why we return the reverse of the result
        # After this backtrack to the top airport in the stack and continue to traaverse it's children

        while len(stack) > 0:
            elem = stack[-1]
            if elem in graph and len(graph[elem]) > 0:
                # Check if elem in graph as there may be a case when there is no out edge from an airport
                # In that case it won't be present as a key in graph
                stack.append(graph[elem].pop())
            else:
                res.append(stack.pop())
                # If there is no further children to traverse then add that airport to res
                # This airport should be the last to go since we can't anywhere from this
                # That's why we return the reverse of the result
        return res[::-1]