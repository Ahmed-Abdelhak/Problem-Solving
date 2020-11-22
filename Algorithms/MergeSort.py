class MergeSort:
      
      def sort(self, arr):
            
            if len(arr) < 2 :
                  return
            
            mid = len(arr) // 2
            
            left = [0] * mid
            for i in range(0, mid):
                left[i] = arr[i]
                
                
            right = [0] * (len(arr) - mid)
            for i in range(mid, len(arr)):
                  right[i-mid] = arr[i]
            
            self.sort(left)
            self.sort(right)
            
            self.__merge(left, right, arr)
      
      def __merge(self,left, right, arr):
            
            i = 0 
            k = 0 
            j = 0
            
            while i < len(left) and j < len(right):
                  if left[i] <= right[j]:
                        arr[k] = left[i]
                        k = k+1
                        i = i+1
                  else:
                        arr[k] = right[j]
                        k = k+1
                        j = j+1

            
            while i < len(left):
                  arr[k] = left[i]
                  k = k+1
                  i = i+1
                  
            while j < len(right):
                  arr[k] = right[j]
                  k = k+1
                  j = j+1


arr = [1, 5, 3, 7, 0, 22, 11, 33, 99 , 77, 10, 2 ]
MergeSort().sort(arr)
print(arr)
