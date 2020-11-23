def LRUCache(strArr):
      cache = [] * 5
       
      for i in range(len(strArr)):
            if strArr[i] not in cache:
                 if len(cache) < 5:
                     cache.append(strArr[i])
                 else:
                       cache.remove(cache[0])
                       cache.append(strArr[i])
            
            else:
                  cache.append(strArr[i])
                  cache.remove(strArr[i])
            
      return cache


print(LRUCache(["A", "B", "C", "D", "E", "D", "Q", "Z", "C"]))
