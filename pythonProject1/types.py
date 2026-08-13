# types.py (new file)
from dataclasses import dataclass
from typing import Any, Dict, Optional

@dataclass
class AnalysisResult:
    builder: Any
    origin_message_id: str
    local_user_ratings: Optional[Dict]
    message_ratings: Dict[str, Dict[str, int]]