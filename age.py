from datetime import datetime
while True:
    print("="*12)
    print("Age Calcutor")
    print("="*12)
    print("")
    while True:
        try:
            boy=int(input("Enter your Birth Year : "))
            break
        except:
            print("Wrong date plz Enter correct birthday")
    today=datetime.today()
    year=int(today.strftime("%y"))
    month=int(today.strftime("%m"))
    day=int(today.strftime("%d"))

    byear=year+2000-boy

    print(f"You are {byear} years old")
