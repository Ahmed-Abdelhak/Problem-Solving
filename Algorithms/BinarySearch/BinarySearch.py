class BinarySearch:
    def __init__(self, el, items):
            self.__el = el
            self.__items = items
            self.__left = 0
            self.__right = len(self.__items) - 1

    def serach(self):
          return self.__search(self.__el,self.__items,self.__left,self.__right)

    # acts as private Method
    def __search(self, el , items, left , right):
      # edge Case 
      # what if passing the element and not found ?  the arr will be shrinked to 0 el
      # in other words {right = arr.length-1 = -1}  , {left = 0}
      if right < left: return -1

      mid = (right + left) // 2
      # base case
      if el == items[mid]: return el
      if el < items[mid]:
            return self.__search(el,items,left, mid-1)
      
      return self.__search(el, items, mid+1, right)

      
print(BinarySearch(3, [1, 2, 3, 4, 5]).serach())  # elements must be sorted
