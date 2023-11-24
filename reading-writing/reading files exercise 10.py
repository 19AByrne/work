f = open("feedback.txt", 'r')
positivecount=0
negativecount=0
feedbackcount = 0
for x in f:
    
    if 'Positive' in x:
        positivecount+=1
        feedbackcount+=1
    elif 'Negative' in x:
        negativecount+=1
        feedbackcount+=1
print(f"Total feedbacks stored in the file {feedbackcount}\nCount of positive feedbacks {positivecount}\nCount of negative feedbacks {negativecount}")