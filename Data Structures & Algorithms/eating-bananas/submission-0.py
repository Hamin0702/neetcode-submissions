class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lowerBound = 1
        upperBound = max(piles)
        minSpeed = upperBound

        while(lowerBound <= upperBound):
            eatingRate = (lowerBound + upperBound) // 2
            totalHours = sum(math.ceil(x/eatingRate) for x in piles)

            if(totalHours <= h and eatingRate < minSpeed):
                    minSpeed = eatingRate

            if(totalHours <= h):
                upperBound = eatingRate - 1
            elif(totalHours > h):
                lowerBound = eatingRate + 1

        return minSpeed

        

