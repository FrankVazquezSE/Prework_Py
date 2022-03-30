#question 1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
'''def hello_name(user_name):
    print("Hello " + user_name + "!")

hello_name('USERNAME')'''
#question 2 Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
'''def first_odds():
    for a in range(1,100):
        if a %2 == 1:
            print(a)

first_odds()'''

#question 3 Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
'''def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max
print (max_num_in_list([1,2,-8,0]))'''
#question 4 Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
'''def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap
    
year = int(input())
print (is_leap(year))'''

#question 5 Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    for num in range(len(a_list)-1):
        if a_list[num+1]!= (a_list[num]+1):
            return False
    return True
print(is_consecutive([2,3,4,5,6,7]))
