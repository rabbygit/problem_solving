class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''

        for index in range(len(strs[0])):
            
            result = result + strs[0][index]
            
            for j in range(1,len(strs)):
                
                if index >= len(strs[j]) or strs[0][index] != strs[j][index]:
                    return result[:-1]

        return result