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
        prompted_part = ("Prompted") if self.prompted else ""
        polarity = "Positive" if self.positive else "Negative"
        additional = ""
        if self.additional_commentary:
            additional = f"- {self.additional_commentary}"
        return (
            f"{self.description} {prompted_part} {additional}"
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
    shorten: str
    positive: List[PositivePillarCharacteristic] = field(default_factory=list)
    negative: List[NegativePillarCharacteristic] = field(default_factory=list)
    grade: int  = None
    added_comments: str = ""

_mand = [ "BA", "AC", "CBP", "COM", "CT", "EP", "CF"]
MANDATORY_PILLARS ={ "MLE": ["ME", "PD", "MM"] + _mand, "MLOps": ["COM", "CT", "EP", "CF"] + _mand, "DS": ["EDA", "ME", "PD", "MM"] + _mand,}
CANDIDATE_TYPES = list(MANDATORY_PILLARS)
MOCK_PILLARS = [    
    Pillars(
        name="Modeling & Evaluation",
        shorten="ME",
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
        shorten="PD",
        description="Ability to deploy models reliably and at scale.",
        positive=[
            PositivePillarCharacteristic(description="Uses Docker or Kubernetes"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Only local deployments"),
        ],
    ),
]


PILLARS = [
    Pillars(
        name="Exploratory Data Analysis (EDA)",
        shorten="EDA",
        description="Ability to explore datasets, identify patterns, anomalies, assumptions, and data quality issues.",
        positive=[
            PositivePillarCharacteristic(description="Systematically checks data types, missing values, and outliers"),
            PositivePillarCharacteristic(description="Uses appropriate visualizations to understand distributions and relationships"),
            PositivePillarCharacteristic(description="Correctly calculates and interprets summary statistics"),
            PositivePillarCharacteristic(description="Formulates hypotheses based on data findings"),
            PositivePillarCharacteristic(description="Identifies data quality issues such as bias or imbalance"),
            PositivePillarCharacteristic(description="Draws meaningful preliminary insights"),
            PositivePillarCharacteristic(description="Effectively uses data analysis and visualization libraries"),
            PositivePillarCharacteristic(description="Uses EDA insights to guide model selection"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Starts modeling without understanding the data"),
            NegativePillarCharacteristic(description="Uses misleading or poorly labeled visualizations"),
            NegativePillarCharacteristic(description="Misses obvious patterns or anomalies"),
            NegativePillarCharacteristic(description="Misinterprets statistics or visualizations"),
            NegativePillarCharacteristic(description="Lacks a structured EDA approach"),
            NegativePillarCharacteristic(description="Draws unsupported conclusions"),
            NegativePillarCharacteristic(description="Chooses models inappropriate for the data"),
        ],
    ),
    Pillars(
        name="Modeling & Evaluation",
        shorten="ME",
        description="""Understanding of ML algorithms, evaluation metrics, and model improvement strategies.\n
Evaluates the candidate's ability to solve algorithmic coding problems, focusing on their problem-solving approach, efficiency (time/space complexity), and ability to articulate their thought process. Mandatory for MLE and MLOps roles, here’s the recommended rationale: 
Solved the problem optimally with no help: 4/4
Solved the problem optimally with help: 3/4
Solved the problem with brute force: 2/4
Did not solve the problem: 1/4
""",
        positive=[
            PositivePillarCharacteristic(description="Explains supervised, unsupervised, and reinforcement learning"),
            PositivePillarCharacteristic(description="Understands bias-variance tradeoff"),
            PositivePillarCharacteristic(description="Selects and justifies appropriate evaluation metrics"),
            PositivePillarCharacteristic(description="Applies model improvement techniques such as tuning and cross-validation"),
            PositivePillarCharacteristic(description="Provides concrete project examples"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Confuses basic ML concepts"),
            NegativePillarCharacteristic(description="Cannot explain bias versus variance"),
            NegativePillarCharacteristic(description="Uses incorrect or unjustified metrics"),
            NegativePillarCharacteristic(description="Limited knowledge of validation techniques"),
            NegativePillarCharacteristic(description="Cannot relate theory to practice"),
        ],
    ),
    Pillars(
        name="Productization & Deployment",
        shorten="PD",
        description="Ability to deploy ML models as scalable and reliable services.",
        positive=[
            PositivePillarCharacteristic(description="Experience with Docker and Kubernetes"),
            PositivePillarCharacteristic(description="Uses ML serving frameworks"),
            PositivePillarCharacteristic(description="Uses optimized model serialization formats"),
            PositivePillarCharacteristic(description="Understands deployment strategies such as blue-green or canary"),
            PositivePillarCharacteristic(description="Experience with cloud ML platforms"),
            PositivePillarCharacteristic(description="Understands APIs, microservices, and scalability"),
            PositivePillarCharacteristic(description="Uses infrastructure as code tools"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Only deploys models locally"),
            NegativePillarCharacteristic(description="No understanding of containers or cloud"),
            NegativePillarCharacteristic(description="Cannot expose models as APIs"),
            NegativePillarCharacteristic(description="Limited understanding of production reliability"),
        ],
    ),
    Pillars(
        name="Model Monitoring",
        shorten="MM",
        description="Knowledge of monitoring models in production and handling performance degradation.",
        positive=[
            PositivePillarCharacteristic(description="Explains feature, label, and concept drift"),
            PositivePillarCharacteristic(description="Tracks predictions and performance metrics"),
            PositivePillarCharacteristic(description="Uses statistical or distribution-based drift detection"),
            PositivePillarCharacteristic(description="Defines actions when performance degrades"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Unaware of production ML maintenance challenges"),
            NegativePillarCharacteristic(description="Cannot explain data drift"),
            NegativePillarCharacteristic(description="No monitoring strategy"),
            NegativePillarCharacteristic(description="Ignores feedback loops and retraining"),
        ],
    ),
    Pillars(
        name="Algorithm Coding",
        shorten="AC",
        description="Problem-solving ability, efficiency, and reasoning during coding tasks.",
        positive=[
            PositivePillarCharacteristic(description="Understands the problem before coding"),
            PositivePillarCharacteristic(description="Breaks problems into smaller steps"),
            PositivePillarCharacteristic(description="Discusses tradeoffs between approaches"),
            PositivePillarCharacteristic(description="Explains algorithms and data structures"),
            PositivePillarCharacteristic(description="Analyzes time and space complexity"),
            PositivePillarCharacteristic(description="Tests edge cases"),
            PositivePillarCharacteristic(description="Communicates reasoning clearly"),
            PositivePillarCharacteristic(description="Uses interviewer hints effectively"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Starts coding without planning"),
            NegativePillarCharacteristic(description="Cannot explain reasoning"),
            NegativePillarCharacteristic(description="Weak understanding of data structures and algorithms"),
            NegativePillarCharacteristic(description="Ignores complexity considerations"),
            NegativePillarCharacteristic(description="Misses edge cases"),
            NegativePillarCharacteristic(description="Gives up easily"),
        ],
    ),
    Pillars(
        name="Coding Best Practices",
        shorten="CBP",
        description="Code quality, readability, maintainability, and idiomatic usage.",
        positive=[
            PositivePillarCharacteristic(description="Writes clean and readable code"),
            PositivePillarCharacteristic(description="Uses meaningful variable and function names"),
            PositivePillarCharacteristic(description="Structures code logically"),
            PositivePillarCharacteristic(description="Follows language conventions"),
            PositivePillarCharacteristic(description="Handles errors properly"),
            PositivePillarCharacteristic(description="Writes modular and reusable code"),
            PositivePillarCharacteristic(description="Uses efficient libraries and tools"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Writes messy or unreadable code"),
            NegativePillarCharacteristic(description="Uses poor naming conventions"),
            NegativePillarCharacteristic(description="Writes monolithic scripts"),
            NegativePillarCharacteristic(description="Uses anti-patterns"),
            NegativePillarCharacteristic(description="Does not handle errors"),
            NegativePillarCharacteristic(description="Produces hard-to-maintain code"),
        ],
    ),
    Pillars(
        name="SQL",
        shorten="SQL",
        description="Ability to query, analyze, and optimize relational databases.",
        positive=[
            PositivePillarCharacteristic(description="Writes correct and efficient SQL queries"),
            PositivePillarCharacteristic(description="Understands relational database concepts"),
            PositivePillarCharacteristic(description="Analyzes execution plans"),
            PositivePillarCharacteristic(description="Writes readable and well-formatted SQL"),
            PositivePillarCharacteristic(description="Handles complex queries"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Cannot write basic SQL queries"),
            NegativePillarCharacteristic(description="Writes inefficient or incorrect SQL"),
            NegativePillarCharacteristic(description="Lacks understanding of joins or indexing"),
            NegativePillarCharacteristic(description="Cannot optimize slow queries"),
            NegativePillarCharacteristic(description="Writes messy SQL"),
        ],
    ),
    Pillars(
        name="Business Acumen",
        shorten="BA",
        description="Ability to connect technical work with business impact.",
        positive=[
            PositivePillarCharacteristic(description="Clearly explains business impact"),
            PositivePillarCharacteristic(description="Uses business metrics"),
            PositivePillarCharacteristic(description="Manages stakeholder expectations"),
            PositivePillarCharacteristic(description="Connects technical decisions to business outcomes"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Focuses only on technical details"),
            NegativePillarCharacteristic(description="Cannot explain business value"),
            NegativePillarCharacteristic(description="Ignores business constraints"),
            NegativePillarCharacteristic(description="Provides generic background"),
        ],
    ),
    Pillars(
        name="Communication",
        shorten="COM",
        description="Clarity, structure, and effectiveness of verbal communication.",
        positive=[
            PositivePillarCharacteristic(description="Provides clear and structured answers"),
            PositivePillarCharacteristic(description="Explains complex topics simply"),
            PositivePillarCharacteristic(description="Uses correct terminology"),
            PositivePillarCharacteristic(description="Speaks fluently and confidently"),
            PositivePillarCharacteristic(description="Demonstrates active listening"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Gives rambling or unclear answers"),
            NegativePillarCharacteristic(description="Overuses jargon"),
            NegativePillarCharacteristic(description="Poor pacing or engagement"),
            NegativePillarCharacteristic(description="Does not answer questions directly"),
        ],
    ),
    Pillars(
        name="Critical Thinking",
        shorten="CT",
        description="Problem-solving and reasoning under ambiguity.",
        positive=[
            PositivePillarCharacteristic(description="Reasons logically in unfamiliar situations"),
            PositivePillarCharacteristic(description="Connects concepts across domains"),
            PositivePillarCharacteristic(description="Asks clarifying questions"),
            PositivePillarCharacteristic(description="Proposes alternative solutions"),
            PositivePillarCharacteristic(description="Remains calm under pressure"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Gives up quickly"),
            NegativePillarCharacteristic(description="Cannot extrapolate knowledge"),
            NegativePillarCharacteristic(description="Becomes defensive when challenged"),
            NegativePillarCharacteristic(description="Lacks structured reasoning"),
        ],
    ),
    Pillars(
        name="English Proficiency",
        shorten="EP",
        description="Ability to communicate effectively in professional English.",
        positive=[
            PositivePillarCharacteristic(description="Uses grammar correctly most of the time"),
            PositivePillarCharacteristic(description="Has sufficient vocabulary range"),
            PositivePillarCharacteristic(description="Speaks fluently"),
            PositivePillarCharacteristic(description="Has clear pronunciation"),
            PositivePillarCharacteristic(description="Understands nuanced discussions"),
        ],
        negative=[
            NegativePillarCharacteristic(description="Frequent grammatical errors"),
            NegativePillarCharacteristic(description="Limited vocabulary"),
            NegativePillarCharacteristic(description="Hesitant or hard-to-understand speech"),
            NegativePillarCharacteristic(description="Pronunciation issues"),
            NegativePillarCharacteristic(description="Difficulty following conversations"),
        ],
    ),
    Pillars(
        name="Cultural Fit",
        shorten="CF",
        description="Cultural fit. Is the candidate a cultural fit with Factored's DNA? Poor Fit (1), Fair Fit (2), Moderate Fit (3) and Perfect Fit (4)",
        positive=[
            PositivePillarCharacteristic(description="Trust, care for, & respect for others"),
            PositivePillarCharacteristic(description="Come As You Are."),
            PositivePillarCharacteristic(description="Deliver Rigor and Excellence, Don’t Be Mediocre."),
            PositivePillarCharacteristic(description="Execution-Focused Meritocracy."),
        ],
    )
]
