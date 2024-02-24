import random

def welcome_user():
  print("Hello! I am your Clothing Store Chatbot!")
  name = input("What is your name?: ")
  print("Nice to meet you, " + name + "!")
  age = input("How old are you?: ")
  print("Great! You are " + age + " years old!")

def show_options():
  print("How can I help you today?")
  print("Option 1: Return item")
  print("Option 2: Feedback")
  print("Option 3: Exchange")
  print("Option 4: Exit chat")


from datetime import datetime

def days_passed():
  start_date_str = input("What is the date you bought the item? (YYYY-MM-DD): ")
  start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

  current_date = datetime.now()
  print("Current date:", current_date)

  change_in_days = current_date - start_date

  days_passed = change_in_days.days

  print("Number of days passed:", days_passed)
  if days_passed > 30:
    print("You have exceeded the 30 day return/exchange period.")
    exit()
  else:
    print("You are within the 30 day return/exchange period.")

  return


def process_return(name):
  print("Hello! " + str(name) + ". I can help you return an item.")
  item_id = input("What is your item ID?(3 digits): ")
  if len(item_id) != 3:
    print("Value is not three digits.")
  else:
      print("Value is three digits.")
  days_passed()
  return_reason = input("What is the reason for your return?(size, damage, other): ")
  if return_reason == "size":
    process_exchange = input("Would you like to exchange?: ")
    if process_exchange == "yes":
      new_size = input("What is your size?: ")
      print("You have exchanged your item for " + new_size + " size.")
      print("Your item has been returned. Thank you for your feedback!")
      return
    elif process_exchange == "no":
      print("Your item has been returned. Thank you for your feedback!")
      return
      
  elif return_reason == "damage":
    process_exchange = input("Would you like to exchange?: ")
    if process_exchange == "yes":
      new_damage = input("Did item come damaged?: ")
      if new_damage == "yes":
        print("You have exchanged your item for " + new_damage + " damage.")
        print("Your item has been returned. Thank you for your feedback!")
        return
      else:
          print("Your item cannot returned.")
          exit()
        
    elif process_exchange == "no":
      print("Your item has been returned. Thank you for your feedback!")
      return
  elif return_reason == "other":
    print("Your item has been returned. Thank you for your feedback!")


def user_feedback(name):
  print("Hello! " + str(name) + ". I can help you return an item.")
  item_id = input("What is your item ID?(3 digits): ")
  if len(item_id) != 3:
    print("Value is not three digits.")
  else:
      print("Value is three digits.")

feedback = input("How was your experience with our service? (good/bad): ")
if feedback == "good":
  print("Thank you for your feedback!")
elif feedback == "bad":
  print("We are sorry to hear that. Please let us know how we can improve.")
  feedback_reason = input("What is the reason for your feedback?: ")
  print( "We will take" + feedback_reason +  "into consideration.")

  
#function for exchange

def proccess_exchange(name):
  print("Hello! " + str(name) + ". I can help you exchange an item.")
  item_id = input("What is your item ID?(3 digits): ")
  if len(item_id) != 3:
    print("Value is not three digits.")
  else:
      print("Value is three digits.")
  days_passed()
  return_reason = input("What is the reason for your return?(size, damage, other): ")
  if return_reason == "size":
    process_exchange = input("Would you like to exchange?: ")
    if process_exchange == "yes":
      new_size = input("What is your size?: ")
      print("You have exchanged your item for " + new_size + " size.")
      print("Your item has been returned. Thank you for your feedback!")
      return
    elif process_exchange == "no":
      print("Your item has been returned. Thank you for your feedback!")
      return

  elif return_reason == "damage":
    process_exchange = input("Would you like to exchange?: ")
    if process_exchange == "yes":
      new_damage = input("Did item come damaged?: ")
      if new_damage == "yes":
        print("You have exchanged your item for " + new_damage + " damage.")
        print("Your item has been returned. Thank you for your feedback!")
        return
      else:
          print("Your item cannot returned.")
          exit()

    elif process_exchange == "no":
      print("Your item has been returned. Thank you for your feedback!")
      return
  elif return_reason == "other":
    print("Your item has been returned. Thank you for your feedback!")
    
def option_response(option, name):
  if option == "1":
      process_return(name)
  elif option == "2":
      user_feedback(name)
    
  elif option == "3":
      proccess_exchange(name)
  elif option == "4":
      print("Goodbye, " + str(name) + "! Have a great day!")
      exit()
  else:
      print("That option is invalid. Please enter a valid option.")


def chatbot():
  
  welcome_user()
  show_options()
  user_option = input("Enter how can I help you today: ")
  name = input("What is your name?: ")
  option_response(user_option,name)

#Start chatbot
chatbot()
  