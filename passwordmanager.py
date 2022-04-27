while True:
    choice=int(input("Enter your choice:\n1. Add Information\n2. View information\n3. Quit\n"))
    if choice==1:
        f = open("students.txt","a")
        name= input("Enter name:")
        grade= input("Enter grade:")
        age=input("Enter age:")
        
        string=f' :_: {name} :_: {grade} :_: {age}\n'
        f.write(string)
    elif choice==2:
        f=open("students.txt","r")
        name=input('Enter name to search info:')
        
        for x in f:
            temp_name=x.split(' :_: ')[0]  
            if name==temp_name:
                grade=x.split(' :_: ')[1]
                age=x.split(' :_: ',' :_: ')[2]
                print(f'Name:{name}')
                print(f'Grade: {grade}')
                print(f'Age: {age}')
                
                
    else:
        break