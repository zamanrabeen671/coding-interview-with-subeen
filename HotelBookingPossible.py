def hotel(arrive, depart, k): 
    arrive.sort()
    depart.sort()

    count = 0
    n = len(arrive)

    i,j = 0,0
    while i < n and j < n:
        if arrive[i] < depart[j] :
            count += 1
            if count > k:
                return False
            i += 1
        else:
            count -= 1
            j += 1
    return True
def hotel_efficent(arrive,depart,k):
    events = [(t,1) for t in arrive] + [(t,0) for t in depart]
    events.sort()

    count = 0
    for event in events:
        if event[1] == 1:
            count += 1
        else:
            count -= 1
        if count > k:
            return False
    return True
if __name__ == "__main__":
    A = [3,5,4,2]
    B = [4,8,6,4]
    print(hotel(A,B,4))
    print(hotel_efficent(A,B,100))