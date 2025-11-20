# Software Department Management System

A console-based application for managing employees and projects in a software department. Track team members, assign them to projects, and generate reports - all from the command line.

## Features

### Employee Management
- Add, update, and remove employees
- Track employee roles, skills, and contact information
- View employee details and current assignments

### Project Management
- Create and manage software projects
- Track project status, technologies, and timelines
- View project teams and member assignments

### Assignment Management
- Assign employees to projects
- Unassign employees and track availability
- View complete project team compositions

### Reports
- Department overview with key metrics
- Employees grouped by role
- Projects grouped by status
- List of unassigned employees

## Installation

1. **Clone or download this repository**

2. **Ensure Python 3.10+ is installed**
   ```powershell
   python --version
   ```

3. **Install dependencies** (optional - this project uses only Python standard library)
   ```powershell
   pip install -r requirements.txt
   ```

## Usage

Run the application from the project directory:

```powershell
python main.py
```

### Quick Start Guide

1. **Main Menu**: Navigate through the main menu by entering numbers 1-5
   - Employee Management
   - Project Management
   - Assignment Management
   - Reports
   - Exit

2. **Adding Employees**: 
   - Navigate to Employee Management > Add Employee
   - Enter employee details (name, role, email, skills)
   - Skills can be entered as comma-separated values

3. **Creating Projects**:
   - Navigate to Project Management > Add Project
   - Provide project name, description, and technologies
   - Set project status (Planning, Active, Testing, Completed, On Hold)

4. **Assigning Employees**:
   - Navigate to Assignment Management > Assign Employee to Project
   - Enter the Employee ID and Project ID
   - The system automatically handles previous assignments

5. **Viewing Reports**:
   - Navigate to Reports to see various analytics
   - Department overview shows key metrics
   - View employees by role or projects by status

## Data Storage

All data is automatically saved to `department_data.json` in the project directory. This file is created automatically on the first save and persists between application sessions.

## Project Structure

```
git-demo/
├── main.py                 # Main application with CLI interface
├── department_manager.py   # Core business logic
├── models/
│   ├── __init__.py
│   ├── employee.py        # Employee data model
│   └── project.py         # Project data model
├── department_data.json   # Data storage (created automatically)
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Example Workflow

1. Add a few employees with different roles (Developer, QA, Manager)
2. Create a software project (e.g., "Mobile App Redesign")
3. Assign employees to the project
4. Update project status as work progresses
5. View reports to track department metrics

## Data Models

### Employee
- ID (auto-generated)
- Name
- Role (e.g., Developer, QA, Manager)
- Email
- Skills (list)
- Hire Date
- Current Project Assignment

### Project
- ID (auto-generated)
- Name
- Description
- Status (Planning, Active, Testing, Completed, On Hold)
- Start Date
- End Date (optional)
- Team Members (list of employee IDs)
- Technologies (list)

## Requirements

- Python 3.10 or higher
- No external dependencies (uses Python standard library only)

## License

This is a sample project for educational purposes.
