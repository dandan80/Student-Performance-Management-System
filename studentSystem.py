import csv
import os

COMMAN_LIST = {"list", "add", "edit", "delete", "average", "exit"}
COURSE_LIST = {"English", "Math", "History" }

#prompt user input operation they want
def get_user_command() -> str:
  while True:
    command = input ("Please input command: ")

#Eliminate upper letters influence
    cmd = command.lower()

    if cmd not in COMMAND_LIST:
       print("Invalid command, please input command: ")
    else:
      return cmd


#load data from file      
def load_data() ->dict:
  file = "student.csv"
  result = {}

#check file is exist
  if os.path.exists(file):
    file_instance = open(file, encoding = 'UTF8')
    csv_reader = csv.DictReader(file_instance)

#read data from file    
    for row in csv_reader:
      name = row.get("name")
      result[name] = row
    return result


#save data to the file   
def save_data(data:dict):
  file = "student.csv"
  file_instance = open(file, 'w', encoding='UTF8')

#if data is not empty
  if len(data) > 0:
    rows = list(data.values())

#create header: the first line in file
    headers = {"name"}.union(COURSE_LIST)
    csv_writer = csv.DictWriter(file_instance, headers)
    csv_writer.writerheader()
    csv_writer.writerows(rows)
  file_instance.close()


#list data in program 
def process_list(student_data: dict):
  records = list(student_data.values())
  records.sort(key=lambda a:a.get('name'))
  
  for record in records:
    print(record.get('name'))
    for course in COURSE_LIST:
      print(f"{course} score: {record.get(course)}")
    print(" ")


#Add data to program    
 def process_add(student_data: dict):
  name = input("Please input student name: ")
  English_score = input("Please input English score: ")
  Math_score = input("Please input Math score: ")
  History_score = input("Please input History score: ")
  
  record = {
      "name": name,
      "English": English_score,
      "Math": Math_score,
      "History": History_score
      }
      
  student_data[name] = record
  print(f"Add student scores for '{name}' successfully")
 

#Edit student score  
def process_edit(student_data:dict):
  name = input("Please input student name: ")
  
  if name in student_data.keys():
    course = input("Please input course name: ")
    
    if course in COURSE_LIST:
      score = input("Please input score: ")
      student_data[name][course]=score
      print(f"Update score for '{name}' successfully")
    else:
      print(f"Course '{course}' is not supported")
      
  else:
    print(f"Student '{name}' does not exist")
    
    
def process_delete(student_data: dict):
  name = input("Please input student name: ")
  
  if name in student_data.keys():
    student_data.pop(name)
  else:
    print(f"Student '{name}' does not exist.")
    
 def process_average(student_data: dict):
   student_count = len (student_data)
   if student_count == 0:
     print("No student scores")
     return 
     
   total_result = {}
   for course in COURSE_LIST:
    total_result[course] = 0
    
   for record in student_data.values():
    for course in COURSE_LIST:
      total_result[course] += int(record.get(course))
      
   for course in COURSE_LIST:
    average = total_result[course] / student_count
    print(f"Average of {course} is: {average}")
    
def process_command(cmd:str, student_data:dict):
  if cmd == 'list':
    process_list(student_data)
  elif cmd = "add":
    process_add(student_data)
  elif cmd = "edit":
    process_edit(student_data)
  elif cmd = "delete":
    process_delete (student_data)
  elif cmd = "average":
    process_average(student_data)
    
    
 def main():
  student_data={}
  #open file try-except
  try:
    student_data = load_data()
  except:
    print("Error happened")
    return
    
  #If 'exit' break loop else continue this program
  while True:
    command = get_user_command()
    if comman == "exit":
      break
    process_command(command, student_data)
 
 #try-except 
  try:
    save_data(student_data)
  except:
    print("Error happened")
    
    
if __name__ = '__main__'
  main()
