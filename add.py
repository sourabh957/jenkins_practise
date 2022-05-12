import sys
import itertools

def permutation(s) : 
    l = s.split(' ') 
    print(l)
    permutations = list(itertools.permutations(l)) 

    print(permutations)


def solve_lower_case(s, t) : 
    t = t.lower() 
    if s == t : 
        return True 
    return False

def solve(s, t) : 
    
    t = t.lower() 
    
    sl = s.split(' ') 
    tl = t.split(' ')

    sl.sort()
    tl.sort() 

    if sl == tl : 
        return True 
    return False

def function(s, temp_test_case) : 
    test_case = [] 

    for str in temp_test_case : 
        str = str.lower()
        test_case.append(str) 
    
    for item in test_case : 
        if item == s : 
            return True
    
    s = s.lower()
    l = tuple(s.split(' ')) 
    permutations = list(itertools.permutations(l)) 
    
    temp_test_case = []
    for item in test_case : 
        temp_string = item.split(' ') 
        temp_test_case.append(tuple(temp_string)) 
    
    for item1 in temp_test_case : 
        for item2 in permutations : 
            if item1 == item2 : 
                return True 
        

    return False 


print(function("a and b", ["B a and", "B and A", "TeXT"])) 

# print(permutation("a and b"))

# print(solve("a and b", "B and A"))

# print(solve_lower_case("text", "Text"))
