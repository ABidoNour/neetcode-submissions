class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        pointer = 0
        result = []
        while pointer < len(s):
            str_len = ""
            while s[pointer] != "#":
                str_len += s[pointer]
                pointer += 1
            str_len = int(str_len)
            curr = s[pointer + 1:pointer+str_len + 1]
            result.append(curr)
            pointer += str_len + 1
        return result


            
