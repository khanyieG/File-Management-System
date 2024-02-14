

def human_resources(path):
    human_resources_path = path / "Human resources"  # Use pathlib for concise path joining
    human_resources_path.mkdir(parents=True, exist_ok=True)
    admin_path = human_resources_path / "Admin"
    admin_path.mkdir(parents=True, exist_ok=True)    
    employee_path= human_resources_path / "Employees"
    employee_path.mkdir(parents=True, exist_ok=True) 
    payements_path= human_resources_path / "Payment"
    payements_path.mkdir(parents=True, exist_ok=True) 
    