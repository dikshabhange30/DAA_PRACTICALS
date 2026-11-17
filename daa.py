# 1) Write a program to calculate Fibonacci numbers and find its step count

n = int(input("Enter the number of terms: "))
a = 0
b = 1
count = 0
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c
    count = count + 1
print("\nStep Count:", count)





# 2) write a program to implement Huffman Encoding using a greedy strategy. / Implement job sequencing with deadlines using a greedy method.
# 1)

import heapq

# Create a node for each character
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

# Function to generate Huffman codes
def generate_codes(root, code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = code if code else "0"
        return

    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)


# Main program
chars = ['A', 'B', 'C', 'D']
freq = [5, 9, 12, 13]

heap = []

for i in range(len(chars)):
    node = Node(chars[i], freq[i])
    heapq.heappush(heap, (freq[i], i, node))

# Build Huffman tree
while len(heap) > 1:
    f1, _, left = heapq.heappop(heap)
    f2, _, right = heapq.heappop(heap)

    new_node = Node(None, f1 + f2)
    new_node.left = left
    new_node.right = right

    heapq.heappush(heap, (new_node.freq, len(heap) + 10, new_node))

# Generate codes
root = heap[0][2]
codes = {}

generate_codes(root, "", codes)

print("Huffman Codes:")
for char in chars:
    print(char, ":", codes[char])

# 2) 
# Job sequencing using Greedy Method

jobs = [
    ('A', 2, 100),
    ('B', 1, 50),
    ('C', 2, 10),
    ('D', 1, 20)
]

# Sort jobs according to profit
jobs.sort(key=lambda x: x[2], reverse=True)

# Find maximum deadline
max_deadline = max(job[1] for job in jobs)

# Create empty time slots
slots = [None] * max_deadline

total_profit = 0

# Select jobs
for job in jobs:
    name, deadline, profit = job

    # Find an empty slot before deadline
    for j in range(deadline - 1, -1, -1):
        if slots[j] is None:
            slots[j] = name
            total_profit += profit
            break

print("Selected Jobs:", slots)
print("Maximum Profit:", total_profit)




# 3) Write a program to solve a fractional Knapsack problem using a greedy method.
# Fractional Knapsack using Greedy Method

weight = [10, 20, 30]
profit = [60, 100, 120]

capacity = 50
total_profit = 0

# Calculate profit/weight ratio
ratio = []

for i in range(len(weight)):
    ratio.append(profit[i] / weight[i])

# Sort items by ratio (highest first)
for i in range(len(ratio)):
    for j in range(i + 1, len(ratio)):
        if ratio[i] < ratio[j]:
            ratio[i], ratio[j] = ratio[j], ratio[i]
            weight[i], weight[j] = weight[j], weight[i]
            profit[i], profit[j] = profit[j], profit[i]

# Select items
for i in range(len(weight)):
    if capacity >= weight[i]:
        total_profit += profit[i]
        capacity -= weight[i]
    else:
        total_profit += ratio[i] * capacity
        break

print("Maximum Profit:", total_profit)





# 4) Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy.
# 0/1 Knapsack using Dynamic Programming

weight = [1, 2, 3]
profit = [10, 15, 40]

capacity = 5
n = len(weight)

# Create a table
dp = [[0] * (capacity + 1) for i in range(n + 1)]

# Fill the table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        if weight[i-1] <= w:
            dp[i][w] = max(
                profit[i-1] + dp[i-1][w-weight[i-1]],
                dp[i-1][w]
            )
        else:
            dp[i][w] = dp[i-1][w]

print("Maximum Profit:", dp[n][capacity])




# 5)Design 8-Queens matrix having first Queen placed. Use backtracking to place remaining Queens to generate the final 8-queen’s matrix.
# 8 Queens Problem using Backtracking

N = 8

board = [[0 for i in range(N)] for j in range(N)]

# Check whether position is safe
def safe(row, col):

    # Check upper column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Place queens using backtracking
def solve(row):

    if row == N:
        return True

    for col in range(N):

        if safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False


# Place first queen at top-left corner
board[0][0] = 1

if solve(1):
    print("8 Queens Solution:")

    for row in board:
        print(row)
else:
    print("No solution found")

