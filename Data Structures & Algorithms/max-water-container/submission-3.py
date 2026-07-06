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
I use two pointers.

One starts from the left.

One starts from the right.

Each time, I calculate the area.

Then I save the bigger area.

After that, I move the shorter side.

Because the shorter side decides the height.

Finally, I return the biggest area.

The time complexity is O(n).

The space complexity is O(1).


"""
        