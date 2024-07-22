from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class MaskingSession:
    session_id: str
    job_seeker_number: str
    recruiter_number: str
    virtual_number: str
    burner_number: str
    expiry_date: str
    last_connected_at: str
    created_at: str = None
    updated_at: str = None

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
