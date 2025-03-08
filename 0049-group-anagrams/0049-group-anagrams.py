class Solution:

    def groupAnagrams(self,strs):
        answer = []
        hashmap = dict()

        if(len(strs)==0):
            return []
        
        for i in range(len(strs)):
            list = [0] * 26
            currentString = strs[i]
            
            for i in range(len(currentString)):
                list[(ord(currentString[i])-ord('a'))]+=1

            s = ""

            for i in range(0,26):
                s+='#'
                s+=str(list[i]) 

            if(s in hashmap):
                hashmap.get(s).append(currentString)
            
            else:
                hashmap[s] = [currentString]
        
        for value in hashmap.values():
            answer.append(value)

        return answer





        