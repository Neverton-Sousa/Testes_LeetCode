class Solution:
    def longestSubarray(self, arr, l):
        i, j, ret = 0, 0, 0
        q1 = deque()  # increasing order deque
        q2 = deque()  # decreasing order deque

        for j in range(len(arr)):
            # Maintain increasing order in q1
            while q1 and arr[q1[-1]] > arr[j]:
                q1.pop()
            q1.append(j)

            # Maintain decreasing order in q2
            while q2 and arr[q2[-1]] < arr[j]:
                q2.pop()
            q2.append(j)

            # Adjust the window when the condition is not met
            while arr[q2[0]] - arr[q1[0]] > l:
                if q2[0] == i:
                    q2.popleft()
                if q1[0] == i:
                    q1.popleft()
                i += 1

            ret = max(ret, j - i + 1)

        return ret