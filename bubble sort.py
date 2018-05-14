list = [5,2,7,4,0,9,8,6]
m = 1

while m < len(list):
     for i in range(len(list)-m):
          if list[i] > list[i+1]:
               list[i],list[i+1] = list[i+1],list[i]
     m += 1
print(list)