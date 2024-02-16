

def human_resources(path):
    '''
    Gaming function contains the scripted folders that will be created for gaming folder
    Parameter: path which it the directory path that is created by user 
    '''

    human_resources_path = path / "Human resources"  
    human_resources_path.mkdir(parents=True, exist_ok=True)
    admin_path = human_resources_path / "Admin"
    admin_path.mkdir(parents=True, exist_ok=True)    
    employee_path= human_resources_path / "Employees"
    employee_path.mkdir(parents=True, exist_ok=True) 
    payements_path= human_resources_path / "Payment"
    payements_path.mkdir(parents=True, exist_ok=True) 
    