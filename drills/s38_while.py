"""
S38 revision drill. Two functions, both from cold. Do not import anything.

1. backoff_steps(gap)
   `gap` is an int, 0 or greater.
   Repeatedly replace gap with (gap // 2).
   Count how many replacements it takes before gap becomes 0, and return
   that count as an int.

       backoff_steps(8) -> 4
           8 // 2 = 4   (1)
           4 // 2 = 2   (2)
           2 // 2 = 1   (3)
           1 // 2 = 0   (4)   gap is now 0, so the answer is 4

       backoff_steps(5) -> 3
           5 -> 2 -> 1 -> 0

2. first_bad(rows)
   `rows` is a list of lists of ints, e.g. [[1, 2], [3, -4, 5], [-1]].
   Go through the rows top to bottom; inside each row go left to right.
   Find the FIRST negative int you meet.
   Return its position as the tuple (row_index, column_index).
   If there is no negative int anywhere in `rows`, return None.

       first_bad([[1, 2], [3, -4, 5], [-1]]) -> (1, 1)
           row 0: 1, 2      - nothing negative
           row 1: 3, -4     - -4 is negative, it sits at row 1, column 1
           so the answer is (1, 1) and nothing after it is looked at
"""


def backoff_steps(gap):
    # I am naming all the 5 step checks here in the comment itself 
    # Boundary : what if the number entered is 0 if that's the case , it doesen't get into the if statement and directly return 0 , same for negative numbers
    # One thing though the negative gaps should also be reduced in the same way as positive gaps , so basically I am changing the function to behave the same way for both side gap
    # khaali case already acccomodated with if != 0 
    # ek here the smalles will be 1 and the function accomodates that as well 
    # bahar is accomodated as well as the function is accomodating negative values as well 
    # the function is doing what mila told actually one step above that , one thing though lets say the user enters something else apart from int , then this will fail 
    
    count = 0 
    if gap!=0:
        gap = abs(gap) # to accomodate and reduce the gap from negative side as well
        while gap>0:
            gap = gap//2
            count +=1
    return count 
    


def first_bad(rows):
    # so the behaviour of this function is basically apart from what it has asked for every other case it returns None 
    number_of_rows = len(rows)
    row_index = 0
     
    while row_index<number_of_rows:
        column_index = 0 
        number_of_columns = len(rows[row_index])
        while column_index<number_of_columns:
            if rows[row_index][column_index]<0:
                return row_index,column_index
            column_index = column_index+1
        row_index = row_index+1
    
        
