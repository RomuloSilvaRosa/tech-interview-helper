from dataclasses import dataclass, field
from typing import List, Literal

@dataclass
class PillarCharacteristic:
    description: str
    positive: bool
    additional_commentary: str = ""
    prompted: bool = False
    checked: bool = False

    def __str__(self):
        prompted_part = "Prompted" if self.prompted else "Spontaneous"
        polarity = "Positive" if self.positive else "Negative"
        return (
            f"{self.description} ({prompted_part})\n"
            f"\n{self.additional_commentary}"
        )

@dataclass
class PositivePillarCharacteristic(PillarCharacteristic):
    positive: Literal[True] = True

@dataclass
class NegativePillarCharacteristic(PillarCharacteristic):
    positive: Literal[False] = False

@dataclass
class Pillars:
    name: str
    description: str
    positive: List[PositivePillarCharacteristic] = field(default_factory=list)
    negative: List[NegativePillarCharacteristic] = field(default_factory=list)
    grade: int | None = None
    added_comments: str = ""
PILLARS = [
    Pillars(
        name="Modeling & Evaluation",
        description="Understanding of ML models, metrics, and evaluation strategies.",
        positive=[
            PositivePillarCharacteristic(description="Chooses correct metrics"),
             PositivePillarCharacteristic(description="Positive 2"),
        ],

        negative=[
            NegativePillarCharacteristic(description="Uses wrong metrics"),
        ],
    ),
    Pillars(
        name="Productization & Deployment",
        description="Ability to deploy models reliably and at scale.",
        positive=[
            PositivePillarCharacteristic(description="Uses Docker or Kubernetes"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Only local deployments"),
        ],
    ),
]
