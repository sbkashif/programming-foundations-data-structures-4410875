""" 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
"""

student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

print(student_pet_count_list)

NUM_OF_STUDENTS = len(student_pet_count_list)

print("Number of students in the class: ", NUM_OF_STUDENTS)

SUM=0
for INDIDVIDUAL_PET_COUNT in student_pet_count_list:
    SUM=SUM+INDIDVIDUAL_PET_COUNT
print(SUM)