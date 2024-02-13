import os
from pathlib import Path

new_folder = input("Name of your new folder: ")

def create_new_dir():
    try:
        os.mkdir(new_folder)
        project_type()
        print(f"folder {new_folder}created.")
    except FileExistsError:
        print(f"folder {new_folder} already exits.")

    return new_folder

def project_type():
    select_folder = str(input("\nWhat kind of project do you want to create?:\nPre Production\nProduction\nPost Production\n")).lower()
    if select_folder == "pre production":
        path = "C:/Users/User1/Documents/Pre-Production"
        os.mkdir(os.path.join(path, "Idea", "Research"))
        os.mkdir(os.path.join(path, "Scripts" ,"Scenario Production"))
        os.mkdir(os.path.join(path, "Storyboarding"))
        os.mkdir(os.path.join(path, "Animatic"))
        os.mkdir(os.path.join(path, "Characters development"))
        os.mkdir(os.path.join(path, "Style framing"))
        pass
    elif select_folder == "production":
        pass
    elif select_folder == "post production":
        pass
    else:
        print("Incorrect input please choose the given names!")
        return project_type()


if __name__ == "__main__":
    create_new_dir()
    # project_type()


























































# from pathlib import Path

# Path.cwd()

# path = ""
# root_dir = os.getcwd

# path = Path("C:/Users/User1")
# path = os.path.realpath(path)
# os.makedirs("Testing")
# os.path.join('C:\\Users\\User1\\Documents', "Testing")

# os.startfile(path)