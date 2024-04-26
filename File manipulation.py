import os

source = 'sample.txt'
destination = "C:\\Users\\Admin\\Desktop\\sample.txt"
if os.path.exists(destination):
    print("There's such file!")
try:
   x = input("What to do in the file? (Move/Delete)")

   if x.lower() == "move":
       os.replace(source,destination)
       print("The File has been Moved!")
   elif x.lower() == "delete":
       os.remove(destination)
       print("The file has been Deleted!")
except FileNotFoundError:
    print(source+" was not found")