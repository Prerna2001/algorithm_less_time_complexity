# O(n) time | O(D) space
# n = total number of elements in the complete array including the subarrays
# D = maximum depth of the given special array

def productSum(array, multiplier=1):
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier+1)
        else:
            sum += element
    return sum * multiplier

