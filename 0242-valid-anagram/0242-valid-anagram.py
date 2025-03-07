class Solution(object):
    def isAnagram(self, s, t):
        charList = []

        for i in range(0,26):
            charList.append(0)

        # check the length of both strings is equal or not 

        if(len(s)!=len(t)):
            return False
        
        for i in range(len(s)):
            index1 = ord(s[i])-ord('a')
            index2 = ord(t[i])-ord('a')


            charList[index1] = charList[index1]+1
            charList[index2] = charList[index2]-1

        for i in charList:
            if(i!=0):
                return False

        return True
        