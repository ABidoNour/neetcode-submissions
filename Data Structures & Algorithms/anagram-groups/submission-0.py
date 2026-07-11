class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dic: dict[str, list] = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in sort_dic:
                sort_dic[sorted_str].append(string)
            else:
                sort_dic[sorted_str]=[string]
        return list(sort_dic.values())