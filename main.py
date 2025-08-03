import json
from datetime import datetime


def add_note():
    try: 

        with open("data.json","r") as f:
            notes = json.load(f)
    except(FileNotFoundError,json.decoder,JSONDecodeError):
        notes = []
    
    # Take user input
    title = input("\nPlease enter the title of your note: ")
    content = input("\n Please enter the content of your note: ")
    timestamp = datetime.now()

    #Create note dictionary
    note = {
        "title":title,
        "content":content, 
        "timestamp": str(timestamp)
    }

    # Append and save to file
    notes.append(note)
    with open("data.json","w") as file:
        json.dump(notes,file,indent=4)



def view_notes():

    #Load and handle empty file
    try:
        with open("data.json","r") as file:
           notes = json.load(file)
    except (FileNotFoundError, json.decoder,JSONDecodeError):
        print("You don't have saved notes!")
        return

    if not notes:
        print("You have no saved notes!")
    else:
        for i , note in enumerate(notes,start=1):
            title = note['title']
            content= note['content']
            timestamp_str = note['timestamp']

            try:

                timestamp_obj = datetime.strptime(timestamp_str,"%Y-%m-%d %H:%M:%S.%f")
                formatted_time = timestamp_obj.strftime("%A, %d %B %Y - %I:%M %p")
            except ValueError:
                formatted_time= timestamp_str
            print(f"{i}. {title} : {content} . (Added on {formatted_time})")

def delete_note():
    #Load the data.json
    with open("data.json","r") as file:
        notes = json.load(file)

    # Show the tasks and ask which one to delete
    view_notes()
    user_choice = input("\nPlease enter the task number you want to delete: ")
    if not user_choice.isdigit():
        print("Please enter a valid number")
        return
    
    task_to_delete = int(user_choice) - 1
    if 0<= task_to_delete < len(notes):
        deleted_note = notes.pop(task_to_delete)
        with open("data.json","w") as file:
            json.dump(notes,file,indent = 4)

        print(f"\n{deleted_note['title']} deleted successfully!")
    else:
        print("Invalid task number!")
        
    #-------------------Menu-------------------
    
menu = ['Add note','View notes','Delete Note', 'Exit']
print(f"\n-----Notes Manager-----")
while True:
    print(f"\n Here is your main menu ")
    for i , option in enumerate(menu,start=1):
       
        
        print(f"{i} . {option}")
       
    
    choice = input("\nEnter the option number you want to open: ")
    
    if not choice.isdigit():
        print("\nEnter the digit please!")
        continue


  
    index = int(choice) - 1
    if 0 <= index < len(menu):
        if index==0:
            add_note()
        elif index==1:
            view_notes()
        elif index==2:
            delete_note()
        else:
            print("Exiting! Thanks for using")
            break
    else:
        print("Invalid Option! Try again please")    
        
    
    

