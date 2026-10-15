class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        oddMax, evenMin = 0, len(s)

        for i in count:
            if count[i]%2 == 0 and count[i] < evenMin:
                evenMin = count[i]
            elif count[i]%2 != 0 and count[i] > oddMax:
                oddMax = count[i]
        
        return oddMax-evenMin
        