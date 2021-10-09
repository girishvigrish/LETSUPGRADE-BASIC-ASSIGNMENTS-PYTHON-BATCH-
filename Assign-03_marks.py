marks = int(input("enter your marks:"))
if 85 <= marks <= 100:
    print('A')
elif 70 <= marks <= 85:
    print('B')
elif 50 <= marks <= 69:
    print('C')
elif 35 <= marks <= 49:
    print('D')
elif marks < 35:
    print('fail')
else:
    print("enter valid marks below 100")