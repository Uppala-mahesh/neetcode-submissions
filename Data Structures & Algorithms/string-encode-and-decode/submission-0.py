class Solution:

    def encode(self, strs: List[str]) -> str:
        en=""
        for i in strs:
            hashh="#"
            
            x=str(len(i))+hashh+i
            en+=x
        return en

    def decode(self, s: str) -> List[str]:
        y=[]
        i=0
        
        
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
        
            num=int(s[i:j])
            
            y.append(s[j+1:j+num+1])
            i=j+num+1
        return y
            


