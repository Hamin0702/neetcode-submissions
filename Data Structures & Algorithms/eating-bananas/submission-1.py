class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lowerBound = 1
        upperBound = max(piles)
        minSpeed = upperBound

        while(lowerBound <= upperBound):
            eatingSpeed = (lowerBound + upperBound) // 2
            totalHours = sum(math.ceil(x/eatingSpeed) for x in piles)

            # if(totalHours <= h and eatingSpeed < minSpeed):
            #         minSpeed = eatingSpeed

            if(totalHours <= h):
                minSpeed = min(minSpeed, eatingSpeed)
                upperBound = eatingSpeed - 1
            elif(totalHours > h):
                lowerBound = eatingSpeed + 1

        return minSpeed

        

