score=0
print("In the followwing questions, you will be asked a question with four options. \nOut of these, one will be the correct answer. \nWrite your option no. after each question. All the best!!!\n")
print("Passing score: 25\n")

#q1
print('''Question 1-
Who is the primary creator of the Python programming language?

1) Guido van Rossum  
2) Larry Page  
3) Mark Zuckerberg  
4) Linus Torvalds
''')

a1= int(input("Option no. here: "))
if a1==1:
    score+=10

#q2
print('''Question 2-
Which of the following statements is used to create a function in Python?

1) def  
2) function  
3) define  
4) func''')

a2= int(input("Option no. here: "))
if a2==1:
    score+=10

#q3
print('''Question 3-
What is the purpose of the "elif" keyword in Python?

1) It represents the end of a conditional statement.  
2) It is short for "else if" and is used for additional conditions in an if-else statement.  
3) It is a syntax error; there is no keyword "elif" in Python.  
4) It is used to define a loop in Python.
''')

a3= int(input("Option no. here: "))
if a3==2:
    score+=10
    
#q4
print('''Question 4-
Which of the following is the correct way to open a file named "example.txt" in read mode in Python?

1) open("example.txt", "r")  
2) read("example.txt", "r")  
3) file("example.txt", "read")  
4) fopen("example.txt", "mode='r'")
''')

a4= int(input("Option no. here: "))
if a4==1:
    score+=10
    
#q5
print('''Question 5-
What is the output of the following code?

```python
x = 10
y = 3

result = x // y

print(result)

1) 3.333
2) 3
3) 3.0
4) 3.5
''')

a5= int(input("Option no. here: "))
if a5==2:
    score+=10
    
print("Your final score:", score)
print("Passing score: 25\n")
if (score>25):
    print("You passed! ")
else:
    print("Failed")
