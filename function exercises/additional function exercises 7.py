#additional function exercises 7
samplelist = [1,2,3,3,3,3,4,5]
def clearduplicates(nums):
    newlist = []
    for x in nums:
        if not x in newlist:
            newlist.append(x)
    return newlist

print(clearduplicates([1,2,3,3,3,3,4,5]))
