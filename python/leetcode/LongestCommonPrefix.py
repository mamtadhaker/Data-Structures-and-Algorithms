class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        minl = min([len(i) for i in strs])
        pre=''
        i = 0
        while i < minl:
            if all(ele[i] == strs[0][i] for ele in strs):
                i += 1
            else:
                break
        return strs[0][:i]