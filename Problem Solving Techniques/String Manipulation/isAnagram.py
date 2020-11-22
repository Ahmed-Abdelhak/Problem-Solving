"""
you have two input words and you want to check whether these two words are permittations for each other , some peaople called them anagrams , so you are required  retrn true or false 
Ex :  input words : "ramy"  , "mary"
reuslt : true 

Ex : "Dogo"  , "Dog"
reuslt is False


# two lengths are the same 
# sort  "ramy" "ramy"          # nlogn
# equality                     # o(n)

Runtime: NlogN , SPACE : o(n)

----------------------------------------------------------------------------------------------


# same length
# iterate over the first dictionary  {'key': value}   key: the character  , value: repition
# iterate over the second 
# if any of the keys of the dict has value bigger than 1 , it will return False

runtime o(N) , Space O(N)





-------------------------------------------------------------------------------

# array.indexOf o(n*m)
 where n is the number of arrays characters 
 and m is the number of characters in the pattern you are seracing for 
 so if you are seachinf for one character it will be o(n)

# substring (int startIndex , int endIndex ) 
      return arr[index]  # o(1)


"mary"  

2 = "ray".indexOf('m')




# array1.length == array2.length
# iterate over the second array
# fetch the index of the current character in the first array
# get this character using "substring" and remove from the first array
# return array1.lenght == 0

"""

def isAnagram(s,t):
      if len(s) != len(t):
            return False

      s = [*s]
      for i in range(len(t)):
            char = t[i]
            index_in_second_arr = s.index(char)
            if index_in_second_arr < 0:
                  return False
            s.remove(char)
            
      return True if len(s) == 0 else False          


print(isAnagram("ramy","mary"))
