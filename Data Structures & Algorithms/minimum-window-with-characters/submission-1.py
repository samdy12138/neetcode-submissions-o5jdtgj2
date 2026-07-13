class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        have = 0
        need_count = len(need)

        l = 0
        ans = ""

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                if ans == "" or r - l + 1 < len(ans):
                    ans = s[l:r + 1]

                left = s[l]
                window[left] -= 1

                if left in need and window[left] < need[left]:
                    have -= 1

                l += 1

        return ans
        