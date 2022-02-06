dic = { }
while True  :
    roll = input("serial no. of the student(enter Q/q if its over): ")
    if roll == "Q" or roll == "q" :
        break
    else :
        name = input("enter the name of student  = ")
        mark = input("enter the marks of student = ")
        dic[roll] = {name , mark}
print(dic)