# iterative solution
class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        idx = 0
        
        for i in range(len(t)):
            if idx == len(s):
                return True
            elif s[idx] == t[i]:
                idx += 1

        return idx == len(s)

# recursion solution
class Solution1:

    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        def dfs(s_idx, t_idx):
            if s_idx == len(s):
                return True
            elif t_idx == len(t):
                return False

            if s[s_idx] == t[t_idx]:
                return dfs(s_idx + 1, t_idx + 1)
            
            return dfs(s_idx, t_idx + 1)

        return dfs(0, 0)