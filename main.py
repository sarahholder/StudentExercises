from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student 
#1. Create 4 or more exercises-----------------------------------------------------
dino_kennel = Exercise('Dino Kennel', 'Javascript')
mushroom_picker = Exercise('Mushroom Picker', 'React')
sorting_hat = Exercise('Sorting Hat', 'Javascript')
sports_roster = Exercise('Sports Roster', 'React')

#2. Create 3, or more, cohorts ----------------------------------------------------
cohort_11 = Cohort('Cohort 11')
cohort_40 = Cohort('Cohort 40')
cohort_1 = Cohort('Cohort 1')   
#3. Create 4, or more, students and assign them to one of the cohorts--------------
sarah_holder = Student('Sarah', 'Holder', 'sarahsmile', 'cohort 40')
davis_lindell = Student('Davis', 'Lindell', 'dlindell', 'Cohort 11')
stephen_castaneda = Student('Stephen', 'Castaneda', 'stephenC', 'Cohort 1')
david_everett = Student('David', 'Everett', 'daveE', 'Cohort 40')
#4. Create 3, or more, instructors and assign them to one of the cohorts.-----------
joe_sheperd = Instructor('Joe', 'Sheperd', 'joes', 'Python')
bryan_nilsen = Instructor('Bryan', 'Nilsen', 'bryan', 'Javascript')
madi_peper = Instructor('Maddie', 'Peper', 'madi', 'Python')
#5. Have each instructor assign 2 exercises to each of the students.
#-------------------------------------------------------------------
joe_sheperd.assign_exercise(sarah_holder, [dino_kennel, mushroom_picker])
joe_sheperd.assign_exercise(davis_lindell, [dino_kennel, sorting_hat])
bryan_nilsen.assign_exercise(stephen_castaneda, [sports_roster, sorting_hat])
madi_peper.assign_exercise(david_everett, [mushroom_picker, sorting_hat])
#Challenge----------------------------------------------------------
exercises = list()
exercises.extend([dino_kennel, mushroom_picker, sorting_hat, sports_roster])

students = list()
students.extend([sarah_holder, davis_lindell, david_everett, stephen_castaneda])

