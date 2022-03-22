# implement the find_sum(lst,k) function which will take a number k as input and return two numbers that add up to k

def find_sum(lst, k):
    # Empty list to be returned if no solution found
    lst_out = []
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[i] + lst[j] == k:
                lst_out = [lst[i], lst[j]]
                break
            else:
                j += 1
        i += 1
    return(lst_out)
