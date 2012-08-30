import random


def check(func):
    test = []
    for i in range(35):
        test.append(random.randint(0, 1000 - 1))
    func(test)
    for i in range(1, len(test)):
        if test[i] < test[i - 1]:
            result = False
    result = True
    print func.__name__, " ", result


def insertsort(num):
    for i in range(1, len(num)):
        j = i - 1
        while num[j] < num[i]:
            j -= 1
        j += 1
        num[j:i + 1] = num[i:i + 1] + num[j:i]


def bublesort(num):
    for i in range(1, len(num)):
        changed = False
        for j in range(1, len(num)):
            if num[j] < num[j - 1]:
                changed = True
                num[j], num[j - 1] = num[j - 1], num[j]
        if not changed:
            break
    return num


def quicksort_r(num, first, last):
    if first >= last:
        return []
    pivot = num[first]
    lesser = [x for x in num[first:last] if x < pivot]
    greater = [x for x in num[first:last] if x > pivot]
    return quicksort_r(lesser, 0, len(lesser)) + [pivot, ] + quicksort_r(greater, 0, len(greater))


def quicksort(num):
    quicksort_r(num, 0, len(num))


def quicksort2(num):
    if num == []:
        return []
    else:
        pivot = num[0]
        lesser = quicksort2([x for x in num[:] if x < pivot])
        greater = quicksort2([x for x in num[:] if x > pivot])
        return lesser + [pivot] + greater


def merge(l1, l2):
    final = []
    while l1 and l2:
        final.append(l1.pop(0) if l1[0] <= l2[0] else l2.pop(0))
    return final + l1 + l2


def mergesort(num):
    mid = int(len(num) / 2)
    if len(num) <= 1:
        return num
    else:
        return merge(mergesort(num[:mid]), mergesort(num[mid:]))
if __name__ == "__main__":
    check(insertsort)
    check(bublesort)
    check(quicksort)
    check(quicksort2)
    check(mergesort)
