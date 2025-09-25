student_name = "Chase"
current_gpa = 3.5
study_hours =  19
social_points = 67
stress_level = 89
user_choice=["Programming", "Math", "English", "History"]
print(f"Welcome {student_name}, your GPA is {current_gpa}, with {study_hours} study hours, {social_points} social points, and  a stress level of {stress_level}")
study_options=["Programming", "Math", "English", "History"]
print("Choose your course load:")
print("A) Light (12 credits)") 
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")


choice= str(input())
study_choice=str(input())
choice_text=''
if choice == "A":
    if  study_hours<stress_level:
      study_hours-=10
      stress_level-=40
      choice_text="A) Light (12 credits)"

    else:
      study_hours-=4
      stress_level-=20
      choice_text="A) Light (12 credits)"
elif choice == "B":
  
 
  study_hours+=3
  stress_level+=5
  choice_text="B) Standard (15 credits)"
elif choice == "C":
  
    if current_gpa>=3.5:
        study_hours+=4
        stress_level+=10
        choice_text="C) Heavy (18 credits)"

    else:
        study_hours+=3
        stress_level+=5
        choice_text="C) Heavy (18 credits)"
else:
      choice_text="ERROR"
   



