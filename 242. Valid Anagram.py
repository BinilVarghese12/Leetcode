class Solution(object):
    def isAnagram(self, s, t):
        counts1 ={}

        for x in range(len(s)):
            character = s[x:(x+1)]
            if character in counts1:
                counts1[character] = counts1[character] +1
            else:
                counts1[character] = 1
        counts2 ={}

        for x in range(len(t)):
            character = t[x:(x+1)]
            if character in counts2:
                counts2[character] = counts2[character] +1
            else:
                counts2[character] = 1

        if counts1 == counts2:
            return True
        else:
            return False