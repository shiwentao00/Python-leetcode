a = [[1,2,3,4],
     [5,6,7,8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]
]

m, n = len(a), len(a[0])

# loop from right up to left down
for d in range(m + n - 1):
    for j in range(d, -1, -1):
        i = d - j
        if i < m and j < n:
            print(a[i][j])
            
print('-----------------------')
# loop from left down to right up
for d in range(m + n - 1):
    for j in range(0, d + 1):
        i = d - j
        if i < m and j < n:
            print(a[i][j])
