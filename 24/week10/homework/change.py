def split_change(change):
    bills=[5,2,1]
    current_change=change
    bills_needed=[]

    for bill in bills:
        bills_needed.append(current_change//bill)
        current_change=current_change%bill
    return bills_needed

print(split_change(11))