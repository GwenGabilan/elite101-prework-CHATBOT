from datetime import date

def welcome_user():
  print("Hello! I am your Chatbot!")
  name = input("What is your name?: ")
  print("Nice to meet you, " + name + "!")
  age = input("How old are you?: ")
  print("Great! You are " + age + " years old!")

def show_options():
  print("How can I help you today?")
  print("Option 1: Info")
  print("Option 2: Todays Date")
  print("Option 3: Fun Fact")
  print("Option 4: Exit chat")

def option_response(option,name):
  if option == "1":
    print( str(name) +"I can tell you information about yadada!")
  elif option == "2":
   #from stacked overflow (https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python)
    today = date.today()
    print(str(name) +",today is " + str(today) + "!")
  elif option == "3":
    print(str(name) +"I can tell you a fun fact about bananas!")
    print("Did you know bananas are slightly radioactive?")
  elif option == "4":
    print("Goodbye, " + str(name) + " ! Have a great day!")
    exit()
  else:
    print("That option is invalid. Please enter a valid option.")

def chatbot():
  
  welcome_user()
  show_options()
  user_option = input("Enter how can I help you today: ")
  name = input("What is your name?: ")
  option_response(user_option,name)
  print("hi")

# Start chatbot
chatbot()
  