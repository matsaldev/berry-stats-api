from dataclasses import dataclass
from typing import Dict, List


@dataclass
class BerryStats:
    berries_names: List[str]
    min_growth_time: float
    median_growth_time: float
    max_growth_time: float
    variance_growth_time: float
    mean_growth_time: float
    frequency_growth_time: Dict[int, int]