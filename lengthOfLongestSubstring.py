class Solution:
    """
    @param: : a string
    @return: an integer
    """

    def lengthOfLongestSubstring(self, s):
        # write your code here
        max_len = -1
        cur_len = 0
        i = 0
        mp = {}
        cur_start = 0
        last_index = 0
        while i < len(s):
            last_index = mp.setdefault(s[i], -1)
            print("---" + s[i] + "---")
            print("last_index = " + str(last_index) + " cur_start = " + str(cur_len))
            if last_index < cur_start:
                mp[s[i]] = i
            else:
                cur_len = i - cur_start
                print("i = " + str(i) + " cur_len = " + str(cur_len))
                if cur_len > max_len:
                    max_len = cur_len
                cur_start = last_index + 1
                mp[s[i]] = i
            i += 1
        if len(s) - cur_start > max_len:
            max_len = len(s) - cur_start
        return max_len


print(Solution().lengthOfLongestSubstring("aafdsafdfga"))
