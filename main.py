"""Main application - Console-based Software Department Management System."""

import os
from department_manager import DepartmentManager


class DepartmentApp:
    """Console application for managing a software department."""
    
    def __init__(self):
        """Initialize the application."""
        self.manager = DepartmentManager()
        self.running = True
    
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title: str):
        """Print a formatted header."""
        print("\n" + "=" * 60)
        print(f"  {title}")
        print("=" * 60 + "\n")
    
    def print_menu(self, title: str, options: list):
        """Print a formatted menu."""
        self.print_header(title)
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        print(f"  {len(options) + 1}. Back")
        print()
    
    def get_input(self, prompt: str, required: bool = True) -> str:
        """Get user input with optional requirement."""
        while True:
            value = input(prompt).strip()
            if value or not required:
                return value
            print("This field is required. Please try again.")
    
    def get_list_input(self, prompt: str) -> list:
        """Get comma-separated list input."""
        value = self.get_input(prompt, required=False)
        if not value:
            return []
        return [item.strip() for item in value.split(',') if item.strip()]
    
    def pause(self):
        """Pause for user to read output."""
        input("\nPress Enter to continue...")
    
    # Main Menu
    def main_menu(self):
        """Display and handle the main menu."""
        while self.running:
            self.clear_screen()
            self.print_header("Software Department Management System")
            print("  1. Employee Management")
            print("  2. Project Management")
            print("  3. Assignment Management")
            print("  4. Reports")
            print("  5. Exit")
            print()
            
            choice = self.get_input("Select an option: ")
            
            if choice == '1':
                self.employee_menu()
            elif choice == '2':
                self.project_menu()
            elif choice == '3':
                self.assignment_menu()
            elif choice == '4':
                self.reports_menu()
            elif choice == '5':
                self.running = False
                print("\nGoodbye!")
            else:
                print("Invalid option. Please try again.")
                self.pause()
    
    # Employee Management
    def employee_menu(self):
        """Employee management menu."""
        while True:
            self.clear_screen()
            options = [
                "Add Employee",
                "View All Employees",
                "View Employee Details",
                "Update Employee",
                "Remove Employee"
            ]
            self.print_menu("Employee Management", options)
            
            choice = self.get_input("Select an option: ")
            
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                self.view_employee_details()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.remove_employee()
            elif choice == '6':
                break
            else:
                print("Invalid option. Please try again.")
                self.pause()
    
    def add_employee(self):
        """Add a new employee."""
        self.clear_screen()
        self.print_header("Add New Employee")
        
        name = self.get_input("Name: ")
        role = self.get_input("Role (e.g., Developer, QA, Manager): ")
        email = self.get_input("Email: ")
        skills = self.get_list_input("Skills (comma-separated): ")
        
        employee = self.manager.add_employee(name, role, email, skills)
        print(f"\n✓ Employee added successfully with ID: {employee.id}")
        self.pause()
    
    def view_all_employees(self):
        """View all employees."""
        self.clear_screen()
        self.print_header("All Employees")
        
        employees = self.manager.list_employees()
        if not employees:
            print("No employees found.")
        else:
            for emp in employees:
                print(f"\n{emp}")
                print("-" * 60)
        
        self.pause()
    
    def view_employee_details(self):
        """View details of a specific employee."""
        self.clear_screen()
        self.print_header("Employee Details")
        
        emp_id = self.get_input("Enter Employee ID: ")
        try:
            employee = self.manager.get_employee(int(emp_id))
            if employee:
                print(f"\n{employee}")
            else:
                print(f"Employee with ID {emp_id} not found.")
        except ValueError:
            print("Invalid ID format.")
        
        self.pause()
    
    def update_employee(self):
        """Update employee information."""
        self.clear_screen()
        self.print_header("Update Employee")
        
        emp_id = self.get_input("Enter Employee ID: ")
        try:
            employee = self.manager.get_employee(int(emp_id))
            if not employee:
                print(f"Employee with ID {emp_id} not found.")
                self.pause()
                return
            
            print(f"\nCurrent details:\n{employee}\n")
            print("Leave blank to keep current value.\n")
            
            name = self.get_input("New name: ", required=False)
            role = self.get_input("New role: ", required=False)
            email = self.get_input("New email: ", required=False)
            skills_str = self.get_input("New skills (comma-separated): ", required=False)
            
            updates = {}
            if name:
                updates['name'] = name
            if role:
                updates['role'] = role
            if email:
                updates['email'] = email
            if skills_str:
                updates['skills'] = [s.strip() for s in skills_str.split(',') if s.strip()]
            
            if updates:
                self.manager.update_employee(int(emp_id), **updates)
                print("\n✓ Employee updated successfully.")
            else:
                print("\nNo changes made.")
        except ValueError:
            print("Invalid ID format.")
        
        self.pause()
    
    def remove_employee(self):
        """Remove an employee."""
        self.clear_screen()
        self.print_header("Remove Employee")
        
        emp_id = self.get_input("Enter Employee ID: ")
        try:
            employee = self.manager.get_employee(int(emp_id))
            if not employee:
                print(f"Employee with ID {emp_id} not found.")
                self.pause()
                return
            
            print(f"\n{employee}\n")
            confirm = self.get_input("Are you sure you want to remove this employee? (yes/no): ")
            
            if confirm.lower() == 'yes':
                self.manager.remove_employee(int(emp_id))
                print("\n✓ Employee removed successfully.")
            else:
                print("\nOperation cancelled.")
        except ValueError:
            print("Invalid ID format.")
        
        self.pause()
    
    # Project Management
    def project_menu(self):
        """Project management menu."""
        while True:
            self.clear_screen()
            options = [
                "Add Project",
                "View All Projects",
                "View Project Details",
                "Update Project",
                "Remove Project"
            ]
            self.print_menu("Project Management", options)
            
            choice = self.get_input("Select an option: ")
            
            if choice == '1':
                self.add_project()
            elif choice == '2':
                self.view_all_projects()
            elif choice == '3':
                self.view_project_details()
            elif choice == '4':
                self.update_project()
            elif choice == '5':
                self.remove_project()
            elif choice == '6':
                break
            else:
                print("Invalid option. Please try again.")
                self.pause()
    
    def add_project(self):
        """Add a new project."""
        self.clear_screen()
        self.print_header("Add New Project")
        
        name = self.get_input("Project name: ")
        description = self.get_input("Description: ")
        technologies = self.get_list_input("Technologies (comma-separated): ")
        
        print("\nStatus options: Planning, Active, Testing, Completed, On Hold")
        status = self.get_input("Status (default: Planning): ", required=False) or "Planning"
        
        project = self.manager.add_project(name, description, technologies, status)
        print(f"\n✓ Project added successfully with ID: {project.id}")
        self.pause()
    
    def view_all_projects(self):
        """View all projects."""
        self.clear_screen()
        self.print_header("All Projects")
        
        projects = self.manager.list_projects()
        if not projects:
            print("No projects found.")
        else:
            for proj in projects:
                print(f"\n{proj}")
                print("-" * 60)
        
        self.pause()
    
    def view_project_details(self):
        """View details of a specific project."""
        self.clear_screen()
        self.print_header("Project Details")
        
        proj_id = self.get_input("Enter Project ID: ")
        try:
            project = self.manager.get_project(int(proj_id))
            if project:
                print(f"\n{project}")
                
                # Show team members
                team = self.manager.get_project_team(int(proj_id))
                if team:
                    print("\nTeam Members:")
                    for emp in team:
                        print(f"  - {emp.name} ({emp.role})")
            else:
                print(f"Project with ID {proj_id} not found.")
        except ValueError:
            print("Invalid ID format.")
        
        self.pause()
    
    def update_project(self):
        """Update project information."""
        self.clear_screen()
        self.print_header("Update Project")
        
        proj_id = self.get_input("Enter Project ID: ")
        try:
            project = self.manager.get_project(int(proj_id))
            if not project:
                print(f"Project with ID {proj_id} not found.")
                self.pause()
                return
            
            print(f"\nCurrent details:\n{project}\n")
            print("Leave blank to keep current value.\n")
            
            name = self.get_input("New name: ", required=False)
            description = self.get_input("New description: ", required=False)
            status = self.get_input("New status: ", required=False)
            tech_str = self.get_input("New technologies (comma-separated): ", required=False)
            
            updates = {}
            if name:
                updates['name'] = name
            if description:
                updates['description'] = description
            if status:
                updates['status'] = status
            if tech_str:
                updates['technologies'] = [t.strip() for t in tech_str.split(',') if t.strip()]
            
            if updates:
                self.manager.update_project(int(proj_id), **updates)
                print("\n✓ Project updated successfully.")
            else:
                print("\nNo changes made.")
        except ValueError:
            print("Invalid ID format.")
        
        self.pause()
    
    def remove_project(self):
        """Remove a project."""
        self.clear_screen()
        self.print_header("Remove Project")
        
        proj_id = self.get_input("Enter Project ID: ")
        try:
            project = self.manager.get_project(int(proj_id))
            if not project:
                print(f"Project with ID {proj_id} not found.")
                self.pause()
                return
            
            print(f"\n{project}\n")
            confirm = self.get_input("Are you sure you want to remove this project? (yes/no): ")
            
            if confirm.lower() == 'yes':
                self.manager.remove_project(int(proj_id))
                print("\n✓ Project removed successfully.")
            else:
                print("\nOperation cancelled.")
        except ValueError:
            print("Invalid ID format.")
        
        self.pause()
    
    # Assignment Management
    def assignment_menu(self):
        """Assignment management menu."""
        while True:
            self.clear_screen()
            options = [
                "Assign Employee to Project",
                "Unassign Employee from Project",
                "View Project Team"
            ]
            self.print_menu("Assignment Management", options)
            
            choice = self.get_input("Select an option: ")
            
            if choice == '1':
                self.assign_employee()
            elif choice == '2':
                self.unassign_employee()
            elif choice == '3':
                self.view_project_team()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")
                self.pause()
    
    def assign_employee(self):
        """Assign an employee to a project."""
        self.clear_screen()
        self.print_header("Assign Employee to Project")
        
        emp_id = self.get_input("Enter Employee ID: ")
        proj_id = self.get_input("Enter Project ID: ")
        
        try:
            if self.manager.assign_to_project(int(emp_id), int(proj_id)):
                print("\n✓ Employee assigned to project successfully.")
            else:
                print("\nFailed to assign. Check if Employee ID and Project ID exist.")
        except ValueError:
            print("Invalid ID format.")
        
        self.pause()
    
    def unassign_employee(self):
        """Unassign an employee from their project."""
        self.clear_screen()
        self.print_header("Unassign Employee from Project")
        
        emp_id = self.get_input("Enter Employee ID: ")
        
        try:
            if self.manager.unassign_from_project(int(emp_id)):
                print("\n✓ Employee unassigned from project successfully.")
            else:
                print("\nFailed to unassign. Check if Employee ID exists or is assigned to a project.")
        except ValueError:
            print("Invalid ID format.")
        
        self.pause()
    
    def view_project_team(self):
        """View all team members of a project."""
        self.clear_screen()
        self.print_header("View Project Team")
        
        proj_id = self.get_input("Enter Project ID: ")
        
        try:
            project = self.manager.get_project(int(proj_id))
            if not project:
                print(f"Project with ID {proj_id} not found.")
                self.pause()
                return
            
            print(f"\nProject: {project.name}")
            print(f"Status: {project.status}\n")
            
            team = self.manager.get_project_team(int(proj_id))
            if team:
                print("Team Members:")
                for emp in team:
                    print(f"\n{emp}")
                    print("-" * 40)
            else:
                print("No team members assigned to this project.")
        except ValueError:
            print("Invalid ID format.")
        
        self.pause()
    
    # Reports
    def reports_menu(self):
        """Reports menu."""
        while True:
            self.clear_screen()
            options = [
                "Department Overview",
                "Employees by Role",
                "Projects by Status",
                "Unassigned Employees"
            ]
            self.print_menu("Reports", options)
            
            choice = self.get_input("Select an option: ")
            
            if choice == '1':
                self.department_overview()
            elif choice == '2':
                self.employees_by_role()
            elif choice == '3':
                self.projects_by_status()
            elif choice == '4':
                self.unassigned_employees()
            elif choice == '5':
                break
            else:
                print("Invalid option. Please try again.")
                self.pause()
    
    def department_overview(self):
        """Show department overview."""
        self.clear_screen()
        self.print_header("Department Overview")
        
        employees = self.manager.list_employees()
        projects = self.manager.list_projects()
        
        assigned = sum(1 for emp in employees if emp.current_project)
        active_projects = sum(1 for proj in projects if proj.status == "Active")
        
        print(f"Total Employees: {len(employees)}")
        print(f"Assigned Employees: {assigned}")
        print(f"Unassigned Employees: {len(employees) - assigned}")
        print(f"\nTotal Projects: {len(projects)}")
        print(f"Active Projects: {active_projects}")
        
        self.pause()
    
    def employees_by_role(self):
        """Show employees grouped by role."""
        self.clear_screen()
        self.print_header("Employees by Role")
        
        employees = self.manager.list_employees()
        roles = {}
        
        for emp in employees:
            if emp.role not in roles:
                roles[emp.role] = []
            roles[emp.role].append(emp)
        
        for role, emps in sorted(roles.items()):
            print(f"\n{role} ({len(emps)}):")
            for emp in emps:
                assigned = f"[Project #{emp.current_project}]" if emp.current_project else "[Unassigned]"
                print(f"  - {emp.name} {assigned}")
        
        self.pause()
    
    def projects_by_status(self):
        """Show projects grouped by status."""
        self.clear_screen()
        self.print_header("Projects by Status")
        
        projects = self.manager.list_projects()
        statuses = {}
        
        for proj in projects:
            if proj.status not in statuses:
                statuses[proj.status] = []
            statuses[proj.status].append(proj)
        
        for status, projs in sorted(statuses.items()):
            print(f"\n{status} ({len(projs)}):")
            for proj in projs:
                team_size = len(proj.team_members)
                print(f"  - {proj.name} [Team: {team_size}]")
        
        self.pause()
    
    def unassigned_employees(self):
        """Show all unassigned employees."""
        self.clear_screen()
        self.print_header("Unassigned Employees")
        
        employees = self.manager.list_employees()
        unassigned = [emp for emp in employees if not emp.current_project]
        
        if not unassigned:
            print("All employees are assigned to projects.")
        else:
            print(f"Found {len(unassigned)} unassigned employee(s):\n")
            for emp in unassigned:
                print(f"{emp.name} - {emp.role}")
                print(f"  Skills: {', '.join(emp.skills) if emp.skills else 'None'}")
                print()
        
        self.pause()
    
    def run(self):
        """Run the application."""
        self.main_menu()


if __name__ == "__main__":
    app = DepartmentApp()
    app.run()
