def selection_sort(li):
   x = len(li)
   
   for i in range(x):
      min_num = i
      for j in range(i + 1, x):
         if li[j] < li[min_num]:
            min_num = j
            
            li[i], li[min_num] = li[min_num], li[i]
   
li = [200, 15, 27, 50,77, 8, 2]
selection_sort(li)
print("The sorted array is:", li)
   