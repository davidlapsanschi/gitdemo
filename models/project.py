"""Project model for the software department."""

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class Project:
    """Represents a software project."""
    
    id: int
    name: str
    description: str
    status: str = "Planning"  # Planning, Active, Testing, Completed, On Hold
    start_date: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    end_date: Optional[str] = None
    team_members: list[int] = field(default_factory=list)
    technologies: list[str] = field(default_factory=list)
    
    def __str__(self) -> str:
        """String representation of the project."""
        tech_str = ", ".join(self.technologies) if self.technologies else "None"
        team_size = len(self.team_members)
        return (f"ID: {self.id} | Name: {self.name}\n"
                f"  Status: {self.status}\n"
                f"  Description: {self.description}\n"
                f"  Technologies: {tech_str}\n"
                f"  Team Size: {team_size}\n"
                f"  Start Date: {self.start_date}\n"
                f"  End Date: {self.end_date or 'Not set'}")
    
    def to_dict(self) -> dict:
        """Convert project to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'team_members': self.team_members,
            'technologies': self.technologies
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Project':
        """Create project from dictionary."""
        return cls(**data)
