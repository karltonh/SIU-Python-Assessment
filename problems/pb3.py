# declare and fill out function here



# test case
#students = {"Drake": 21, "Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
#print(youngest_student2(students))  # Expected output: "Alice"

def youngest_student(students):
  student_names = list(students)
  maxAge = students[student_names[0]]
  maxName = student_names[0]
  for names in student_names:
      if students[names] > maxAge:
          maxAge = students[names]
          maxName = names

  return maxName