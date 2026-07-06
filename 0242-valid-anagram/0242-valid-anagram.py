class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fre1 = {}
        fre2 = {}
        for i in s:
            fre1[i]=fre1.get(i,0)+1

        for j in range(len(t)):
            if t[j] in fre2:

                fre2[t[j]] += 1

            else:
                fre2[t[j]] = 1

        return(fre1 == fre2)
