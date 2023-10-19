class Solution:
    def candy(self, ratings: List[int]) -> int:

        #GREEDY APPROACH?

        n = len(ratings)
        total = 1
        for i in range(n):
            left = right = -1
            if i - 1 >= 0:
                left = ratings[i - 1]
            if i + 1 < n:
                right = ratings[i + 1]

            if (ratings[i] >= left or left == -1) and (ratings[i] >= right or right == -1):
                total += 2
            else:
                total += 1

        return total
    
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 2 pass solution
        memo = [1] * len(ratings)
        n = len(ratings)

        #Forward Pass (Compare Left Neighbors)
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                memo[i] = memo[i - 1] + 1
            
        #Backwards Pass (Compare Right Neighbors)
        for i in range(n - 2, -1, -1 ):
            if ratings[i] > ratings[i + 1]:
                # We need to take the max here since memo[i + 1] is dependent the ones before it
                memo[i] = max(memo[i], memo[i + 1] + 1)
        
        return sum(memo)

############################################################################################################################################
# 
# Copied One Pass Solution - 
# Credit (https://leetcode.com/problems/candy/solutions/4037646/99-20-greedy-two-one-pass/?envType=study-plan-v2&envId=top-interview-150)
#
############################################################################################################################################

# Why Up, Down, and Peak?
# The essence of the one-pass greedy algorithm lies in these three variables: Up, Down, and Peak. They serve as counters for the following:

# Up: Counts how many children have increasing ratings from the last child. This helps us determine how many candies we need for a child with a higher rating than the previous child.

# Down: Counts how many children have decreasing ratings from the last child. This helps us determine how many candies we need for a child with a lower rating than the previous child.

# Peak: Keeps track of the last highest point in an increasing sequence. When we have a decreasing sequence after the peak, we can refer back to the Peak to adjust the number of candies if needed.

# How Does it Work?
# Initialize Your Counters
# Start with ret = 1 because each child must have at least one candy. Initialize up, down, and peak to 0.
# Loop Through Ratings
# For each pair of adjacent children, compare their ratings. Here are the scenarios:

# If the rating is increasing: Update up and peak by incrementing them by 1. Set down to 0. Add up + 1 to ret because the current child must have one more candy than the previous child.

# If the rating is the same: Reset up, down, and peak to 0, because neither an increasing nor a decreasing trend is maintained. Add 1 to ret because the current child must have at least one candy.

# If the rating is decreasing: Update down by incrementing it by 1. Reset up to 0. Add down to ret. Additionally, if peak is greater than or equal to down, decrement ret by 1. This is because the peak child can share the same number of candies as one of the children in the decreasing sequence, which allows us to reduce the total number of candies.

# Return the Total Candy Count
# At the end of the loop, ret will contain the minimum total number of candies needed for all the children, so return ret.
# By using up, down, and peak, we can efficiently traverse the ratings list just once, updating our total candies count (ret) as we go. This method is efficient and helps us solve the problem in a single pass, with a time complexity of O(n)O(n)O(n).

# Time and Space Complexity
# Time Complexity: O(n)O(n)O(n), for the single pass through the ratings array.
# Space Complexity: O(1)O(1)O(1), as we only use a few extra variables.
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        
        ret, up, down, peak = 1, 0, 0, 0
        
        for prev, curr in zip(ratings[:-1], ratings[1:]):
            if prev < curr:
                up, down, peak = up + 1, 0, up + 1
                ret += 1 + up
            elif prev == curr:
                up = down = peak = 0
                ret += 1
            else:
                up, down = 0, down + 1
                ret += 1 + down - int(peak >= down)
        
        return ret