print('''
Welcome to Saint John's Northwestern Military Academy!
This is your Academic Planner Program that will help you keep your assignments in line
''')

homework_to_do=[]
homework_due_dates=[]

tests_quizzes=[]
tests_quiz_dates=[]

while(True):
    '''
    problem 1)
    '''
    user_input = int(input("?"))

    if user_input == 1 : homework_to_do.append (input("What is your assigned homework? >>>"))
    if user_input == 1 : homework_due_dates.append (input("When is the homework due? >>>"))
    if user_input == 2 : tests_quizzes.append (input("What is the topic of your next quiz/test? >>>"))
    if user_input == 2 : tests_quiz_dates.append (input("When are you taking that test? >>>"))
    if user_input == 3 : 
        print("---Homework---")
        print(homework_to_do)
        print(homework_due_dates)
        print("---Quizzes---")
        print(tests_quizzes)
        print(tests_quiz_dates)
    print ("Have a Nice Day!")


