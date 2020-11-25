def reverse_words(str):
    reverse_chars(str, 0, len(str) -1 )
    
    start_index = 0
    for i in range(len(str)):
         if( i == len(str) or str[i] == ' '):
              reverse_chars(str, start_index, i-1)
              start_index = i + 1
       
 
def reverse_chars(str, start_index, end_index):
     
     i = start_index
     j = end_index

     while (i < j):
          str[i], str[j] = str[j], str[i]
          i = i+1
          j = j-1





 
print(reverse_words(['c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l']))
