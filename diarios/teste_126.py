class Solution(object):
    def getLucky(self, s, k):
        string = ""
        for i in s: # "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
            string += str(ord(i) - ord('a') + 1)
        
        for _ in range(k):
            digit_sum = 0

            for i in string:            #Transform 1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
                digit_sum += int(i)                #Transform 2: 17 ➝ 1 + 7 ➝ 8

            string = str(digit_sum)
        
        return int(string)