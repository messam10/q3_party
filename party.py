people = []
i = 0
z = 3

while i < z:
  x = input("Enter name : ")
  people.append(x)
  if(i == z-1):
    y =input("Do you want add another? Y|N  ")
    if(y == "Y"):
        z+=1
    elif(y == "N"):
        print("People in Party :")
        print(people)
    else:
        print("Error enter Y or N")
  i += 1

