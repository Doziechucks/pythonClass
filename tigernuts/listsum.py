arrayOne = [3, 4, 9, 19, 4, 1]
arrayTwo = [1, 5, 7, 8]
def list_sum(arrayOne, arrayTwo):
   arrayOne.sort()
   arrayTwo.sort()
   countOne = 0
   countTwo = 0
   list = []
   while countOne < len(arrayOne) and countTwo < len(arrayTwo):
      if arrayOne[countOne] < arrayTwo[countTwo]:
         list.append(arrayOne[countOne])
         countOne += 1
      else:
         list.append(arrayTwo[countTwo])
         countTwo += 1
   while(countOne < len(arrayOne)):
         list.append(arrayOne[countOne])
         countOne += 1

   while(countTwo < len(arrayTwo)):
         list.append(arrayTwo[countTwo])
         countTwo += 1
   
   return list
print(list_sum(arrayOne, arrayTwo))
   
   
     