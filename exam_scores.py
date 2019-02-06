# This program will let user input their Score in numbers 
# then output what grade they got.
# 90 or above = A
# 80 or above = B
# 70 or above = C
# 60 or above = D
# Below 60 = F

while True:
    print("This program will calculate what grade you got based on your SCORE.\n")
    
    grade = eval(input('Please, enter your score: '))
    if (grade > 100 or grade < 0):
        print("\n!!!!!!\nNumbers need to be between 100 and 0")
        continue
    else:
        break

if grade >= 90:
    print('your grade is A')
elif grade >= 80:
    print('your grade is B')
elif grade >= 70:
    print('your grade is C')
elif grade >= 60:
    print('your grade is D')
elif grade < 60:
    print('your grade is F')
