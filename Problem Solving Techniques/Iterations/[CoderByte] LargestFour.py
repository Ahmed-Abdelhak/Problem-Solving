def largest_four(arr):
      sum = 0
      if len(arr) < 5 :
            for i in arr:
                  sum = sum + i
      else:
            arr.sort()
            i = len(arr) - 1
            while i > (len(arr) - 5):
                  sum = sum + arr[i]
                  i = i - 1
                  
      return sum


print(largest_four([4, 5, -2, 3, 1, 2, 6, 6]))
