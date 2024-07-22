from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class BurnerToReal:
    burner_number: str
    real_number: str
    expiry_date: str
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
