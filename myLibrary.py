def greatestof3Values(n1,n2,n3):
    maximum = n1
    if maximum < n2:
        maximum = n2
    if maximum < n3:
        maximum = n3
    return (f"{maximum} is the greates value of {n1}, {n2}, and {n3}.")