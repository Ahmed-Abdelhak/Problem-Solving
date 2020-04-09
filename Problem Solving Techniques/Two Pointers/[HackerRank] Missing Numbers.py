# Sample Input

# 10
# 203 204 205 206 207 208 203 204 205 206
# 13
# 203 204 204 205 206 207 205 208 203 206 205 206 204
# Sample Output

# 204 205 206


def missingNumbers(arr, brr):
    result = set()
    k = 0
    for i in range(len(brr)):
        if k >= len(arr):
            result.add(brr[i])
        elif arr[k] == brr[i]:
            k = k+1
        else:
            result.add(brr[i])

    return sorted(result)


print(missingNumbers([11, 4, 11, 7, 13, 4, 12, 11, 10, 14], [
      11, 4, 11, 7, 3, 7, 10, 13, 4, 8, 12, 11, 10, 14, 12]))
