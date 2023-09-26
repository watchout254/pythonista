student_data = [
     {
         "name": "dan",
         "roll_no": 12,
         "age":21,
         "course": "python"
      },
    {
        "name":"mukenya",
        "roll_no": 15,
        "age":22,
        "course": "data science"
     },
]

def add_new_student(name,roll_no,age,course):
   new_student = {}
   new_student["name"]=name
   new_student["roll_no"]=roll_no
   new_student["age"]=age
   new_student["course"]=course
   student_data.append(new_student)

add_new_student("shyam",22,18,"C++")
print(student_data)



