from problems import example
from problems import pb1, pb2, pb3

def main():
    pass
    print('ding dong')
    #example.testFunc()
    print(pb1.replace_spaces('test str', 'p'))
    print(pb2.max_values([1,2,3,4,5,6]))
    students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20, "Karl": 23}
    print(pb3.youngest_student(students))
    # Test Cases

    # Problem #1: Replace Spaces
    # sentence = "Test  This is a test   Testing "
    # sentence2 = pb1.replace_spaces(sentence, "_")
    # print(sentence2)

    # Problem #2: Max Values
    # print(pb2.max_values([-5, -2, -1, -11])) # -> [1, 2]  

    # Problem #3: Youngest Student
    # students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
    # print(pb3.youngest_student(students))  # Expected output: "Alice"

#def replace_spaces(stringToReplace, replaceSpaceWith):
#    newStr = stringToReplace.replace(' ',replaceSpaceWith)
#    print(newStr)
#    return newStr
    
#def max_values(values):
#    a = values[0]
#    for v in values:
#        if v > a: 
#            a = v
#    b = values[0]        
#    values.remove(a)  
#    for n in values:
#        if n > b: 
#            b = n
#
#    maxV = [a,b]
#    print(maxV)      
#    return maxV

#def youngest_student(students):
#    student_names = list(students)
#    maxAge = students[student_names[0]]
#    maxName = student_names[0]
#    for names in student_names:
#        if students[names] > maxAge:
#            maxAge = students[names]
#            maxName = names

#    print(maxName)
#    return maxName
if __name__ == '__main__':
     main()
