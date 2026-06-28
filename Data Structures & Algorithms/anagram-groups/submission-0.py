class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaf={}
        for s in strs:
            sk="".join(sorted(s))
            if sk not in anaf:
                anaf[sk]=[]
            anaf[sk].append(s)
        return list(anaf.values())

        