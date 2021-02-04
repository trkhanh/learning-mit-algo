# Input : 10 20 15
#         21 30 14
#         7  16 32
# Output : 30
# 30 is a peak element because all its
# neighbors are smaller or equal to it.
# 32 can also be picked as a peak.

# Input : 10 7
#         11 17
# Output : 17

# Finding peak element in a 2D Array.
from math import ceil
MAX = 100

# Function to find the maximum in column 'mid'
# 'rows' is number of rows.


def findMax(arr, rows, mid, max):

    max_index = 0
    for i in range(rows):
        if(max < arr[i][mid]):

            # Saving global maximum and its index
            # to check its neighbours
            max = arr[i][mid]
            max_index = i
        # print(max_index)
    return max, max_index

# Function to find a peak element


def findPeakRec(arr, rows, columns, mid):
    max = 0
    max, max_index = findMax(arr, rows, mid, max)

    if(mid == 0 or mid == columns - 1):
        
# A wrapper over findPeakRec()


def findPeak(arr, rows, columns):
    return findPeakRec(arr, rows,
                       columns, columns // 2)


# Driver Code
arr = [[10, 8, 10, 10],
       [14, 13, 12, 11],
       [15, 9, 11, 21],
       [16, 17, 19, 20]]

# Number of Columns
rows = 4
columns = 4
print(findPeak(arr, rows, columns))
