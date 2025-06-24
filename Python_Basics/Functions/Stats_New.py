
'''
Functions for Statistics in python, Functions to find mean of data
'''


# Functions to find median of data Using while loop
def nk_mean(l):
    """This functions take list as input and returns the mean value of that list"""
    n = len(l)
    sum1 = 0
    x = 0
    while x < n:
        sum1 = sum1 + l[x]
        x = x + 1
    mean = sum1 / n
    return(mean)


# Functions to find median of data Using for loop
def the_mean(pass_list):
    """This functions take list as input and returns the mean value of that list"""
    len_list = len(pass_list)
    sum_items = 0
    for num in pass_list:
        sum_items = sum_items + num
    mean_list = sum_items/len_list
    return mean_list


l1 = [23, 44, 23, 12, 45, 62, 7, 9, 34, 98, 12, 23, 12]
print("Mean of l1 : ", nk_mean(l1))
print("Mean of l1 : ", the_mean(l1))


# Functions to find median of data
def nk_median(l):
    """This function returns the median of the list"""
    n = len(l)
    if n % 2 == 0:
        p = int(n / 2)
        x = l[p - 1]
        y = l[p]
        median = (x + y) / 2
        return(median)
    else:
        p = int((n + 1) / 2)
        median = l[p - 1]
        return(median)


def the_median(pass_list):
    """This function returns the median of the list"""
    len_list = len(pass_list)
    if len_list % 2 == 0:
        half_length = int(len_list/2)
        first_middle = pass_list[half_length]
        second_middle = pass_list[half_length - 1]
        median  = (first_middle + second_middle) /  2
        return median
    else:
        mid_index = int((len_list + 1) / 2)
        median = pass_list[mid_index-1]
        return median

print("Median of l1 : ", nk_median(l1))
print("Median of l1 : ", the_median(l1))

l1 = [23, 44, 23, 12, 45, 62, 7, 9, 34, 98, 12, 23, 12]


# Functions to find mode of data method -1
def the_mode(pass_list):
    """This function returns the mode of the list"""
    count = []
    items = []
    for num in pass_list:
        count_times = 0
        if num in items:
            continue
        for value in pass_list:
            if num == value:
                count_times += 1
        count.append(count_times)
        items.append(num)
    mode = []
    for i in range(len(count)):
        if count[i] == max(count):
            mode.append(items[i])
    return mode
print("Mode of Passed List : ", the_mode(l1))


# Functions to find mode of data method -2 using collections module
from collections import Counter

def find_mode(lst):
    # Use Counter to count the frequency of each element in the list
    counts = Counter(lst)
    print(type(counts))
    print(counts)
    
    # Find the maximum count
    max_count = max(counts.values())
    print(max_count)
    print(counts.items())
    
    # Find all elements with the maximum count (the mode)
    mode = [key for key, value in counts.items() if value == max_count]
    
    return mode

# Example usage:
l1 = [23, 44, 23, 12, 45, 62, 7, 9, 34, 98, 12, 23, 12]
mode_result = find_mode(l1)
print("Mode of Passed List : ", mode_result)

# Functions to find varience

# Method - 1
def the_varience(pass_list):
    """This functions take list as input and returns the varience of that list"""
    len_list = len(pass_list)
    sum1 = 0
    x = 0
    while x < len_list:
        sum1 = sum1 + pass_list[x]
        x = x + 1
    mean = sum1 / len_list
    numerator = [(num - mean) ** 2 for num in pass_list]
    variance = sum(numerator) / (len_list - 1)
    return (variance)

# Example usage:
print("Varience of l1 : ", the_varience(l1))

# Method - 2
def nk_varience1(pass_list):
    """This functions take list as input and returns the varience of that list"""
    len_list = len(pass_list)
    numerator = [(num - the_mean(pass_list)) ** 2 for num in pass_list]
    variance = sum(numerator) / (len_list - 1)
    return (variance)

# Example usage:
print("Varience of l1 : ", nk_varience1(l1))


# Functions to find Standard deviation

# Method - 1
def find_stddev(pass_list):
    """This functions take list as input and returns the standard deviation of that list"""
    sd = (the_varience(pass_list))**(1/2)
    return sd

# Example usage:
print("Standard Deviation of l1 : ", find_stddev(l1))

# Method - 2
def the_stddev(pass_list):
    """This functions take list as input and returns the standard deviation of that list"""
    import math
    sd = math.sqrt(the_varience(pass_list))
    return sd

# Example usage:
print("Standard Deviation of l1 : ", the_stddev(l1))

# Functions to find Z-score

def the_zscore(pass_list):
    """This functions take list as input and returns the Z-score of that list"""
    z_score = [(num - nk_mean(pass_list)) / the_stddev(pass_list) for num in pass_list]
    return z_score

# Example usage:
print("Z-score of l1 : ", the_zscore(l1))
