# https://www.bigocheatsheet.com/

# Runtime Analysis
# all about relationship between # of items vs # of steps

# n = number of steps

# Constant -> O(1)
def print_one_item(items):
    print(items[0])

# Linear -> O(n)
def print_every_item(items):
    for item in items:
        print(item)

# if inputted 5 items, output (# of times looped through) of 25
# Quadratic -> O(n^2)
def print_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)


# overall run time O(n^2) due to being the highest run time
                        #  n
def do_a_bunch_of_stuff(items): 
    last_idx = len(items) - 1 # 0(1)
    print(last_idx) # 0(1)

    for item in items:
        print(item) # 0(1)

    for item in items: # O(n)
        for item in items: # O(n)
            print(item, item) # 0(1)
    # ^ added up times = O(n^2) run time

    middle_idx = len(items) / 2 # 0(1)
    idx = 0 # 0(1)
    while idx < middle_idx: # O(n/2)
        print("something") # O(1)
        idx = idx + 1 # O(1)


"""
Big O is the worst case
"""
def search_for_thing(items, thing):
    for item in items:
        if item == thing:
            return True

    return False