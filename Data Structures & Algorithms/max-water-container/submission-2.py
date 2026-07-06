class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        res=0
        while l<r:
            area=(r-l)*min(heights[l],heights[r])
            res=max(res,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res
"""
I use two pointers, one from the left and one from the right.

Each time, I calculate the area using the width and the smaller height.

Then I update the max area.

I move the pointer with the smaller height, 
because the smaller height limits the area.

If the left height is smaller, I move left.

Otherwise, I move right.

Finally, I return the max area.

The time complexity is O(n), and the space complexity is O(1).

"""
        