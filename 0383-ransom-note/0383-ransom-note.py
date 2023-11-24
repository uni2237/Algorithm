class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict={}
        for k in set(ransomNote):
            ransom_dict[k]=0

        magazine_dict={}
        for k in set(magazine):
            magazine_dict[k]=0

        for i in ransomNote:
            ransom_dict[i]+=1

        for i in magazine:
            magazine_dict[i]+=1

        for k in ransom_dict.keys():
            if k not in magazine_dict.keys():
                return False
            elif ransom_dict[k]>magazine_dict[k]:
                return False
            else:
                continue
        return True

        