import os
import shutil

cwd = os.getcwd()

print("What would you like to cleanup?")
print("1: Desktop")
print("2: Downloads")
choice = input("Enter Choice: ")

if choice == "1":
    dir_path = (r'C:\Users\alexb\OneDrive\Desktop') #Set to your own desktop location
    os.chdir(dir_path)
    items = os.listdir()  # List all items in the directory

    for item in items:
        item_path = os.path.join(dir_path, item)

        if os.path.isdir(item_path):
            continue

        # Extract file extension, default to 'Other'
        ext = os.path.splitext(item)[1][1:] or 'Other'
        folder_name = os.path.join(dir_path, ext)

        # see if folder exists if not make one
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        dest_path = os.path.join(folder_name, item)

        #move the file
        shutil.move(item_path, dest_path)
    print("All cleaned up!")
        
if choice == "2":
    dir = (r'C:\Users\alexb\Downloads') # set to your own downloads location
    os.chdir(dir)
    items = os.listdir()  # List all items in the directory

    for item in items:
        item_path = os.path.join(dir, item)

        if os.path.isdir(item_path):
            continue

        # Extract file extension, default to 'Other'
        ext = os.path.splitext(item)[1][1:] or 'Other'
        folder_name = os.path.join(dir, ext)

        # see if folder exists if not make one
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        dest_path = os.path.join(folder_name, item)

        #move the file
        shutil.move(item_path, dest_path)
    print("All cleaned up!")