class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters : dict[str,int] = {}
        t_letters : dict[str,int] = {}
        for letter in s:
            if letter in s_letters:
                s_letters[letter]+=1
            else:
                s_letters[letter]=1
        for letter in t:
            if letter in t_letters:
                if t_letters.get(letter)==s_letters.get(letter):
                    return False
                if letter not in s_letters:
                    return False
                t_letters[letter]+=1
            else:
                t_letters[letter]=1
        if len(s_letters)!=len(t_letters):
            return False
        for letter in s_letters.keys():
            if s_letters.get(letter) != t_letters.get(letter):
                return False
        return True