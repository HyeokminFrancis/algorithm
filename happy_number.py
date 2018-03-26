# finding happy number
def dec_instances(number):
    
    dec_each = []
    
    while number != 0:
    
        dec_each.append(number % 10)
        number = int(number/10)
    
    return dec_each


def is_happy_number(number):
    
    
    # use set, cause in operator average time comp is O(1) on set
    # it does not matter that numbers are duplicate in this set

    set_number = set()
    
    #should check out if it is looping infinitely
    while number not in set_number and number != 1:
    
        set_number.add(number)
    
        a = list(map((lambda x:x**2),dec_instances(number)))
        number = sum(a)
    
    
    return number == 1
        