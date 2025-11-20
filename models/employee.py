"""Employee model for the software department."""

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class Employee:
    """Represents an employee in the software department. SOmething nice"""
    
    id: int
    name: str
    role: str
    email: str
    skills: list[str] = field(default_factory=list)
    hire_date: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    current_project: Optional[int] = None
    
    def __str__(self) -> str:
        """String representation of the employee."""
        skills_str = ", ".join(self.skills) if self.skills else "None"
        return (f"ID: {self.id} | Name: {self.name} | Role: {self.role}\n"
                f"  Email fancy: {self.email}\n"
                f"  Skills: {skills_str}\n"
                f"  Hire Date: {self.hire_date}\n"
                f"  Current Project: {self.current_project or 'Unassigned'}")
    
    def to_dict(self) -> dict:
        """Convert employee to dictionary for JSON serialization."""





        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'email': self.email,
            'skills': self.skills,
            'current_project': self.current_project
        }

    # fancy print function
    def fancy_print(self) -> None:
        """Print employee details in a fancy format."""
        print("===================================")
        print(f"Employee ID: {self.id}")
        print(f"Name       : {self.name}")
        print(f"Role       : {self.role}")
        print(f"Email      : {self.email}")
        print(f"Skills     : {', '.join(self.skills) if self.skills else 'None'}")
        print(f"Hire Date  : {self.hire_date}")
        print(f"Current Project: {self.current_project or 'Unassigned'}")
        print("===================================")





    
    @classmethod
    def from_dict(cls, data: dict) -> 'Employee':
        """Create employee from dictionary."""
        return cls(**data)
