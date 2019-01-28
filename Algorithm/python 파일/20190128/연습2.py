def brute_force(array, key):
   for i in range(len(array)-len(key)+1):
       j = i
       for k in key:
           if k != array[j]:
               break
           else:
               j += 1
       else:
           return i

   return False

array = "abcdefghjikejejrkewrhjkewhrkhejkr"
key = 'jk'
print(brute_force(array,key))