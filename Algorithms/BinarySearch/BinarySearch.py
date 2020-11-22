class BinarySearch:
    def __init__(self, el, items):
            self.__el = el
            self.__items = items
            self.__left = 0
            self.__right = len(self.__items) - 1

    def serach_recursive(self):
          return self.__search_recursive(self.__el,self.__items,self.__left,self.__right)

    # acts as private Method
    def __search_recursive(self, el , items, left , right):
      # edge Case 
      # what if passing the element and not found ?  the arr will be shrinked to 0 el
      # in other words {right = arr.length-1 = -1}  , {left = 0}
      if right < left: return -1

      mid = (right + left) // 2
      # base case
      if el == items[mid]: return el
      if el < items[mid]:
            return self.__search_recursive(el,items,left, mid-1)
      
      return self.__search_recursive(el, items, mid+1, right)


    def search(self, el, arr):
          left = self.__left
          right = self.__right
            
          while( left <= right):
                mid = (left + right) // 2
                if el < arr[mid] :
                      right = mid -1
                elif el > arr[mid]:
                      left = mid -1
                else:
                      return arr[mid]
                  
          return -1
          
          
      
            
      
print(BinarySearch(3, [1, 2, 3, 4, 5]).serach_recursive())  # elements must be sorted
