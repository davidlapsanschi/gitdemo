"""Employee model for the software department."""

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class Employee:
    """Represents an employee in the software department."""
    
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
                f"  Email: {self.email}\n"
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
            'hire_date': self.hire_date,
            'current_project': self.current_project
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Employee':
        """Create employee from dictionary."""
        return cls(**data)
