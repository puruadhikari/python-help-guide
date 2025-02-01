"""
You are a developer for a university. Your current project is to develop a system for students to find
courses they share with friends. The university has a system for querying courses students are enrolled in,
returned as a list of (ID, course) pairs .
Write a function that takes in a list of (student ID number, course name) pairs and returns,
for every pair of students, a list of all courses they share.

NOTE, IMP : See how set is used to get the intersections of two items
NOTE : See the clever use of combinations and set
"""
student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]

student_course_pairs_2 = [
  ["42", "Software Design"],
  ["0", "Advanced Mechanics"],
  ["9", "Art History"],
]

from collections import defaultdict
from itertools import combinations
student_dict = defaultdict(set)

for student, course in student_course_pairs_2:
    student_dict[student].add(course)


all_students = student_dict.keys()
all_combination = list(combinations(all_students,2))
output = defaultdict(list)
for student1,student2 in all_combination:
  common_course = list(student_dict[student1] & student_dict[student2])
  output[(student1,student2)] = common_course

print(output)