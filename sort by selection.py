def mymin(mylist):
    for k in range(len(mylist) - 1):
        m = k
        i = k + 1
        while i < len(mylist):
            if mylist[i] < mylist[m]:
                m = i
            i += 1
        t = mylist[k]
        mylist[k] = mylist[m]
        mylist[m] = t