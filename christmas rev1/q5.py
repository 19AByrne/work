#christmas revision exercise 1 q5
sec = int(input("Enter seconds: "))
hours = (sec//60)//60
minutes = (sec//60)%60
seconds = sec%60
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
