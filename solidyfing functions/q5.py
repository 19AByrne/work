import myMathLib

while 1:
    print('''1)circle area
2)circle perimeter
3)rectangle area
4)rectangle perimeter''')
    choice = int(input())
    if choice == 1:
        print(myMathLib.circle_area(int(input('Enter diameter: '))))
    elif choice == 2:
        print(myMathLib.perimeter_circle(int(input('Enter diameter: '))))
    elif choice == 3:
        print(myMathLib.rectangle_area(int(input('Enter height: ')),int(input('Enter width: '))))
    elif choice == 4:
        print(myMathLib.rectangle_perimeter(int(input('Enter height: ')),int(input('Enter width: '))))