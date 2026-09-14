from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Lead:
    business_name: str = ""
    person_name: str = ""
    source: str = ""
    source_url: str = ""
    original_text: str = ""
    website: Optional[str] = None
    industry: str = ""
    location: str = ""
    intent: str = ""
    opportunity_score: int = 0
    score_label: str = ""
    reason: str = ""
    public_contact: str = ""
    status: str = "Needs review"

    def to_dict(self):
        return asdict(self)
