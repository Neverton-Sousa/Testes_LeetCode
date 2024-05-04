class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the array to simplify the boat allocation process
        people.sort()

        # Initialize two pointers, one at the beginning and one at the end of the array
        left = 0  # Pointer for the lightest person
        right = len(people) - 1  # Pointer for the heaviest person
        boats_count = 0  # Count of boats required

        # Iterate until both pointers meet or cross each other
        while left <= right:
            # If both the lightest and heaviest persons can fit in the same boat
            if people[left] + people[right] <= limit:
                boats_count += 1  # Allocate a boat
                left += 1  # Move to the next lightest person
                right -= 1  # Move to the next heaviest person
            # If only the heaviest person can fit in a boat
            elif people[right] <= limit:
                boats_count += 1  # Allocate a boat
                right -= 1  # Move to the next heaviest person

        return boats_count  # Return the total count of boats required


# 881. Boats to Save People
# Medium
# Topics
# Companies
# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.


# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
