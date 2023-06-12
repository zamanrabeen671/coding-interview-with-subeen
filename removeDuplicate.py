def remove_duplicates(arr): 
   n = len(arr)
   current_index = 1
   for i in range(1, n): 
      if arr[i] != arr[i-1]: 
         arr[current_index] = arr[i]
         current_index += 1
   return current_index

if __name__ == "__main__" :
   
   my_array = [1,1,2,3,3]
   result = remove_duplicates(my_array)
   print(result)
