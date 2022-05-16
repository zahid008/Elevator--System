import time
floor = int(input("Enter the floor: "))
flag = 1
i=-1

while flag:
  if(i<floor):
    for i in range(i+1,floor+1):
        print(i)
      #time.sleep(1)
  elif(i>floor):
    for i in range(i-1,floor-1,-1):
      print(i)
      #time.sleep(1)
  #print(i)
  floor = int(input("Enter the floor: "))
