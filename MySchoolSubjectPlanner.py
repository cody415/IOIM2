# My School Subject Planner

# Step 1: Store fixed student details in a tuple
student_details = ("Aparna Desai", "Grade 10", "Roll No: 23")
print("Student Details:", student_details)

# Access tuple values
print("Student Name:", student_details[0])
print("Class:", student_details[1])
print("Roll Number:", student_details[2])

# Step 2: Create subject sets for different days
monday_subjects = {"Math", "English", "Science"}
tuesday_subjects = {"Math", "History", "Science", "Art"}
wednesday_subjects = {"English", "Geography", "Science"}

print("\nMonday Subjects:", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)
print("Wednesday Subjects:", wednesday_subjects)

# Step 3: Modify sets
# Add a subject
monday_subjects.add("Computer Science")
print("\nAfter Adding to Monday:", monday_subjects)

# Remove a subject
tuesday_subjects.remove("Art")
print("After Removing from Tuesday:", tuesday_subjects)

# Step 4: Compare subjects using set operations
# Common subjects between Monday and Tuesday
common_mon_tue = monday_subjects.intersection(tuesday_subjects)
print("\nCommon Subjects (Mon & Tue):", common_mon_tue)

# Subjects unique to Wednesday
unique_wed = wednesday_subjects.difference(monday_subjects.union(tuesday_subjects))
print("Unique Wednesday Subjects:", unique_wed)

# All subjects across three days
all_subjects = monday_subjects.union(tuesday_subjects, wednesday_subjects)
print("All Subjects (Mon, Tue, Wed):", all_subjects)

# Symmetric difference (subjects in Mon or Tue but not both)
sym_diff_mon_tue = monday_subjects.symmetric_difference(tuesday_subjects)
print("Subjects in Mon or Tue but not both:", sym_diff_mon_tue)
