"""Department Manager - Core business logic for managing the software department."""

import json
from typing import Optional, List
from pathlib import Path
from models import Employee, Project


class DepartmentManager:
    """Manages employees and projects in the software department."""
    
    def __init__(self, data_file: str = "department_data.json"):
        """Initialize the department manager."""
        self.data_file = Path(data_file)
        self.employees: dict[int, Employee] = {}
        self.projects: dict[int, Project] = {}
        self.next_employee_id = 1
        self.next_project_id = 1
        self.load_data()
    
    # Employee Management
    def add_employee(self, name: str, role: str, email: str, skills: List[str]) -> Employee:
        """Add a new employee to the department."""
        employee = Employee(
            id=self.next_employee_id,
            name=name,
            role=role,
            email=email,
            skills=skills
        )
        self.employees[employee.id] = employee
        self.next_employee_id += 1
        self.save_data()
        return employee
    
    def get_employee(self, employee_id: int) -> Optional[Employee]:
        """Get an employee by ID."""
        return self.employees.get(employee_id)
    
    def list_employees(self) -> List[Employee]:
        """List all employees."""
        return list(self.employees.values())
    
    def update_employee(self, employee_id: int, **kwargs) -> bool:
        """Update employee information."""
        employee = self.get_employee(employee_id)
        if not employee:
            return False
        
        for key, value in kwargs.items():
            if hasattr(employee, key) and value is not None:
                setattr(employee, key, value)
        
        self.save_data()
        return True
    
    def remove_employee(self, employee_id: int) -> bool:
        """Remove an employee from the department."""
        if employee_id not in self.employees:
            return False
        
        # Remove from any projects
        employee = self.employees[employee_id]
        if employee.current_project:
            project = self.get_project(employee.current_project)
            if project and employee_id in project.team_members:
                project.team_members.remove(employee_id)
        
        del self.employees[employee_id]
        self.save_data()
        return True
    
    # Project Management
    def add_project(self, name: str, description: str, technologies: List[str], status: str = "Planning") -> Project:
        """Add a new project."""
        project = Project(
            id=self.next_project_id,
            name=name,
            description=description,
            technologies=technologies,
            status=status
        )
        self.projects[project.id] = project
        self.next_project_id += 1
        self.save_data()
        return project
    
    def get_project(self, project_id: int) -> Optional[Project]:
        """Get a project by ID."""
        return self.projects.get(project_id)
    
    def list_projects(self) -> List[Project]:
        """List all projects."""
        return list(self.projects.values())
    
    def update_project(self, project_id: int, **kwargs) -> bool:
        """Update project information."""
        project = self.get_project(project_id)
        if not project:
            return False
        
        for key, value in kwargs.items():
            if hasattr(project, key) and value is not None:
                setattr(project, key, value)
        
        self.save_data()
        return True
    
    def remove_project(self, project_id: int) -> bool:
        """Remove a project."""
        if project_id not in self.projects:
            return False
        
        # Unassign employees
        project = self.projects[project_id]
        for emp_id in project.team_members:
            employee = self.get_employee(emp_id)
            if employee and employee.current_project == project_id:
                employee.current_project = None
        
        del self.projects[project_id]
        self.save_data()
        return True
    
    # Assignment Management
    def assign_to_project(self, employee_id: int, project_id: int) -> bool:
        """Assign an employee to a project."""
        employee = self.get_employee(employee_id)
        project = self.get_project(project_id)
        
        if not employee or not project:
            return False
        
        # Remove from previous project if assigned
        if employee.current_project:
            old_project = self.get_project(employee.current_project)
            if old_project and employee_id in old_project.team_members:
                old_project.team_members.remove(employee_id)
        
        # Assign to new project
        employee.current_project = project_id
        if employee_id not in project.team_members:
            project.team_members.append(employee_id)
        
        self.save_data()
        return True
    
    def unassign_from_project(self, employee_id: int) -> bool:
        """Unassign an employee from their current project."""
        employee = self.get_employee(employee_id)
        if not employee or not employee.current_project:
            return False
        
        project = self.get_project(employee.current_project)
        if project and employee_id in project.team_members:
            project.team_members.remove(employee_id)
        
        employee.current_project = None
        self.save_data()
        return True
    
    def get_project_team(self, project_id: int) -> List[Employee]:
        """Get all employees assigned to a project."""
        project = self.get_project(project_id)
        if not project:
            return []
        
        return [self.employees[emp_id] for emp_id in project.team_members 
                if emp_id in self.employees]
    
    # Data Persistence
    def save_data(self):
        """Save all data to JSON file."""
        data = {
            'next_employee_id': self.next_employee_id,
            'next_project_id': self.next_project_id,
            'employees': {str(k): v.to_dict() for k, v in self.employees.items()},
            'projects': {str(k): v.to_dict() for k, v in self.projects.items()}
        }
        
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_data(self):
        """Load data from JSON file."""
        if not self.data_file.exists():
            return
        
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            
            self.next_employee_id = data.get('next_employee_id', 1)
            self.next_project_id = data.get('next_project_id', 1)
            
            self.employees = {
                int(k): Employee.from_dict(v) 
                for k, v in data.get('employees', {}).items()
            }
            
            self.projects = {
                int(k): Project.from_dict(v) 
                for k, v in data.get('projects', {}).items()
            }
        except Exception as e:
            print(f"Error loading data: {e}")
