import random


def firstNonRepeatingElement(arr, n):
    for i in range(n):
        j = 0
        while(j < n):
            if(i != j and arr[i] == arr[j]):
                break
            j += 1
        if(j == n):
            return arr[i]
    return -1


arr = random.sample(range(20, 30), 20)
print(arr)
n = len(arr)
print(firstNonRepeatingElement(arr, n))
