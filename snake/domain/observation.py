from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Observation:
    up: List[str]
    left: List[str]
    down: List[str]
    right: List[str]
        
