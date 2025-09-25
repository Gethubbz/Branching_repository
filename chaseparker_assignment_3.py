student_name = "Chase"
current_gpa = 3.5
study_hours =  19
social_points = 67
stress_level = 89
user_choice=["Programming", "Math", "English", "History"]
print(f"Welcome {student_name}, your GPA is {current_gpa}, with {study_hours} study hours, {social_points} social points, and  a stress level of {stress_level}")
#Part1, adds or subtracts to your current social points, study hours, GPA, and your level of stress, along with my name
study_options=["Programming", "Math", "English", "History"]
print("Choose your course load:")
print("A) Light (12 credits)") 
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

#Part2, I used conditionals and relational operators to decide what credit level using the choice(input) variable
#it depicts how much you study and the level of stress due to your credits, 
#with being the highest for it being C at 24 hrs and 99 for stress.
#This also give results for chocie_text, which will be used for later terms
choice= str(input("Your choice: "))
study_choice=str(input("Your choice: Programming, Math, English, or History : "))
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




#Part3, Based on the results, another operator named study_choice will ask you to pick between 
#"Programming", "Math", "English", "History" 
#and once picked your option, your social pooitns and GPA will be thourgougly edited,
#with some like programming having a specific conditional if the person chose C, 
#with it being even more difficult or B with the same logic
# I used membership and logical operators to represent these different changes

#Part4 is implimemted with the indentions and different options
#creating a possiblity of 6 endings plus the final test using 
#identity oeprators as it checks if your study 
#hours share a value with your social points with History having this honor
#Final statistics are also presented
if study_choice in study_options or not(study_choice==None):
    if study_choice=="Programming" and choice_text=="C) Heavy (18 credits)":
       current_gpa+=0.4
       social_points-=10

    elif study_choice=="Programming":
        current_gpa+=0.2
        social_points-=5
    
    if study_choice=="History":
       current_gpa+=0.3
       social_points=study_hours

    elif study_choice=="Math":
       current_gpa+=0.1
       social_points-=6
    
    if study_choice=="English" and choice_text=="B) Standard (15 credits)":
       current_gpa+=0.1
       social_points-=2
    elif study_choice=="English":
       current_gpa+=0.1
       social_points-=1
    
    if study_hours is social_points:
       current_gpa-=0.2
       social_points+=2
    elif study_hours is not social_points:
       current_gpa-=0.1
       social_points+=3

elif study_choice not in study_options:
       current_gpa+=0
       social_points-=0
print(choice_text)
print(f"your GPA: {current_gpa:.1f}")
print(f"your hours: {study_hours}")
print(f"your stress: {stress_level}")
print(f"your social life: {social_points}")



