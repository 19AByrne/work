#task 9 next question
mystr = input("Enter any word with an odd amount of characters ")
midchar = mystr[len(mystr)//2]
firstchar = mystr[len(mystr)//2-1]
thirdchar = mystr[len(mystr)//2+1]
final = (firstchar+midchar+thirdchar)
print(final)