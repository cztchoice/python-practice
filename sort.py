import random


#def insertsort(num):
    #"""
    #This insert is wrong, because it cannot take the insertsort's advantage
    #that O(1) complex when the list have been sorted
    #"""
    #for i in range(1, len(num)):
        #j = 0
        #while num[j] < num[i]:
            #j += 1
        #if j < i:
            ##temp = [num[i], ] + num[j:i]
            ##num[j:i + 1] = temp
            #num[j:i + 1] = num[i:i + 1] + num[j:i]
    #return num

def insertsort(num):
    for i in range(1, len(num)):
        for j in range(i, 0, -1):
            if num[j] < num[j - 1]:
                num[j], num[j - 1] = num[j - 1], num[j]
            else:
                break
    return num


def selectsort(num):
    for i in range(0, len(num) - 1):
        temp = i
        for j in range(i, len(num)):
            if num[temp] > num[j]:
                temp = j
        num[temp], num[i] = num[i], num[temp]
    return num


def bublesort(num):
    for i in range(1, len(num)):
        for j in range(1, len(num)):
            if num[j] < num[j - 1]:
                num[j], num[j - 1] = num[j - 1], num[j]
    return num


def partion(num, first, last):
    sep = first
    pivot = num[sep]
    index = first
    num[sep], num[last] = num[last], num[sep]
    for i in range(first, last):
        if num[i] < pivot:
            num[i], num[index] = num[index], num[i]
            index += 1
    num[index], num[last] = num[last], num[index]
    return index


def quicksort_r(num, first, last):
    if first > last:
        return
    index = partion(num, first, last)
    quicksort_r(num, first, index - 1)
    quicksort_r(num, index + 1, last)
    return


def quicksort(num):
    quicksort_r(num, 0, len(num) - 1)
    return num


def mergesort_r(num, first, last):
    if first >= last:
        return
    pivot = (first + last) / 2
    mergesort_r(num, first, pivot)
    mergesort_r(num, pivot + 1, last)
    temp = num[:]
    i = j = 0
    k = pivot
    while i < len(temp) & j < pivot & k < last:
        if temp[j] < temp[k]:
            num[i] = temp[j]
            i += 1
            j += 1
        else:
            num[i] = temp[k]
            i += 1
            k += 1
    else:
        if j < pivot:
            num[i:] = temp[j:pivot]
        if k < last:
            num[i:] = temp[k:last]


def mergesort(num):
    mergesort_r(num, 0, len(num))
    return num


def check(num):
    for i in range(1, len(num)):
        if num[i] < num[i - 1]:
            return False
    return True

if __name__ == "__main__":
    test = []
    for i in range(25):
        test.append(random.randint(0, 1000 - 1))
    temp = test[0:len(test)]
    temp = insertsort(temp)
    print "Insertsort: ", check(temp)

    temp = test[0:len(test)]
    temp = selectsort(temp)
    print "Seclectsort: ", check(temp)

    temp = test[0:len(test)]
    temp = bublesort(temp)
    print "Bublesort: ", check(temp)

    temp = test[0:len(test)]
    temp = quicksort(temp)
    print "Quicksort: ", check(temp)

    temp = test[0:len(test)]
    temp = mergesort(temp)
    print "Mergesort: ", check(temp)
