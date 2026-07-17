class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))
            encoded += "#"
            encoded += s
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
            pointer += 1
            curr = s[pointer:pointer+str_len]
            result.append(curr)
            pointer += str_len
        return result


            
