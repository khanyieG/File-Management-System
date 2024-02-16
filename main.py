from pathlib import Path
from animation import *
from human_resources import *
from gaming import *


def create_new_dir():

    '''
    Create new directory function is were we get the use input to create a new folder/directory
    '''

    new_folder = input("Name of your new folder: ")
    new_dir = Path(new_folder)
    try:
        new_dir.mkdir(parents=True, exist_ok=True)
        project_type(new_dir)
        print(f"Folder created: {new_dir}")
    except FileExistsError:
        print(f"folder {new_folder} already exits.")

    return new_folder

def project_type(path):

    ''' 
    project type function is where we want to know what kind of a project/folder do they want in 
    in there new directory

    parameter: path of the new directory created by the user
    '''

    select_folder = str(input("\nWhat kind of project do you want to create?:\nAnimation\nGaming\nhuman resources\n")).lower()
    if select_folder == "animation":
        animation(path)
        
    elif select_folder == "gaming":
        gaming(path)

    elif select_folder == "human resources":
        human_resources(path)
    
    else:
        print("Incorrect input please choose the given names!")
        return project_type(path)


if __name__ == "__main__":
    create_new_dir()
    