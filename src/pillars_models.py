from dataclasses import dataclass, field
from typing import List, Literal

@dataclass
class PillarCharacteristic:
    description: str
    
    positive: bool
    additional_commentary: str = ""
    prompted: bool = False
    checked: bool = False
    didnt_modifier: bool = False
    comment: bool = False
    

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
    def __post_init__(self):
        self.positive = sorted(
            self.positive,
            key=lambda c: c.description.lower()
        )
        self.negative =     sorted(
            self.negative,
            key=lambda c: c.description.lower()
        )

_mand = [ "BA", "AC", "CBP", "COM", "CT", "EP", "CF", "SR"]
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
    ),
    Pillars(
    name="Seniority",
    shorten="SR",
    description="Assesses the candidate’s seniority level based on experience, problem framing, execution style, handling of ambiguity, system thinking, business awareness, and communication maturity.",
    positive=[
        # LEVEL I — JUNIOR
        PositivePillarCharacteristic(
            description="Level I – Experience (1–3 years): Early-career engineer focused on learning fundamentals and executing well-defined tasks with guidance."
        ),
        PositivePillarCharacteristic(
            description="Level I – Focus on the What: Prioritizes delivering the correct answer to the question asked rather than exploring alternatives or implications."
        ),
        PositivePillarCharacteristic(
            description="Level I – Seeks Concrete Answers: Most comfortable with factual, closed-ended questions; struggles with ambiguity and ill-defined problems."
        ),
        PositivePillarCharacteristic(
            description="Level I – Execution-Oriented: Jumps directly into implementation without significant problem reframing or validation."
        ),
        PositivePillarCharacteristic(
            description="Level I – Theory Handling: Can provide textbook definitions (e.g., bias and variance) but struggles to contextualize them in real-world scenarios."
        ),
        PositivePillarCharacteristic(
            description="Level I – Open-Ended Questions: Tends to propose the first solution that comes to mind and may get stuck if it is not viable."
        ),
        PositivePillarCharacteristic(
            description="Level I – Coding Approach: Writes functional code for the happy path but may overlook edge cases, efficiency, or structure."
        ),
        PositivePillarCharacteristic(
            description="Level I – Technical Expertise: Developing; understands concepts but lacks depth from real-world experience."
        ),
        PositivePillarCharacteristic(
            description="Level I – Critical Thinking: Relies on known patterns and struggles with novel or ambiguous problems."
        ),
        PositivePillarCharacteristic(
            description="Level I – Business Acumen: Low; describes work in terms of tasks completed rather than business impact."
        ),
        PositivePillarCharacteristic(
            description="Level I – Communication: Explains what was done but often lacks the strategic why behind decisions."
        ),

        # LEVEL II — MID-LEVEL
        PositivePillarCharacteristic(
            description="Level II – Experience (3–5 years): Reliable and independent contributor capable of owning well-scoped tasks end to end."
        ),
        PositivePillarCharacteristic(
            description="Level II – Focus on the How: Goes beyond the final answer to explain how a solution would be implemented."
        ),
        PositivePillarCharacteristic(
            description="Level II – Developing Awareness: Recognizes trade-offs and can discuss basic alternatives based on prior experience."
        ),
        PositivePillarCharacteristic(
            description="Level II – Task Ownership: Can be trusted to deliver multiple tasks and knows when to ask for help."
        ),
        PositivePillarCharacteristic(
            description="Level II – Theory Handling: Provides correct answers and adds practical context (e.g., multiple techniques for class imbalance and which were used before)."
        ),
        PositivePillarCharacteristic(
            description="Level II – Open-Ended Questions: Breaks problems into manageable parts and proposes logical solutions, sometimes needing prompting to explore more options."
        ),
        PositivePillarCharacteristic(
            description="Level II – Coding Approach: Writes clean, well-structured code, considers some edge cases, and can analyze time and space complexity."
        ),
        PositivePillarCharacteristic(
            description="Level II – Technical Expertise: Solid command of core tools and concepts."
        ),
        PositivePillarCharacteristic(
            description="Level II – Critical Thinking: Strong within well-defined problem spaces."
        ),
        PositivePillarCharacteristic(
            description="Level II – Business Acumen: Growing; understands how their work impacts project goals."
        ),
        PositivePillarCharacteristic(
            description="Level II – Communication: Clear and concise; effectively explains thought process and technical decisions."
        ),

        # LEVEL III — MID-SENIOR
        PositivePillarCharacteristic(
            description="Level III – Experience (5–7 years): Comfortable leading the technical direction of projects and working effectively under ambiguity."
        ),
        PositivePillarCharacteristic(
            description="Level III – Focus on the Why: Naturally connects technical decisions to underlying reasons and business goals."
        ),
        PositivePillarCharacteristic(
            description="Level III – Problem Framing: Asks clarifying questions to ensure the right problem is being solved before implementation."
        ),
        PositivePillarCharacteristic(
            description="Level III – System-Level Thinking: Considers scalability, monitoring, maintenance, and architectural fit."
        ),
        PositivePillarCharacteristic(
            description="Level III – Theory Handling: Uses theoretical questions as a starting point to discuss trade-offs grounded in experience."
        ),
        PositivePillarCharacteristic(
            description="Level III – Open-Ended Questions: Systematically deconstructs ambiguity, compares multiple viable solutions, and justifies decisions using clear criteria."
        ),
        PositivePillarCharacteristic(
            description="Level III – Coding Approach: Designs robust solutions first, considering validation, error handling, efficiency, and maintainability."
        ),
        PositivePillarCharacteristic(
            description="Level III – Technical Expertise: High depth and breadth of knowledge."
        ),
        PositivePillarCharacteristic(
            description="Level III – Critical Thinking: Excellent ability to navigate and resolve ambiguity independently."
        ),
        PositivePillarCharacteristic(
            description="Level III – Business Acumen: Frames technical choices in terms of business impact, cost, speed, and value."
        ),
        PositivePillarCharacteristic(
            description="Level III – Communication: Structured, persuasive, and well-tailored to the audience."
        ),

        # SENIOR+
        PositivePillarCharacteristic(
            description="Senior+ – Experience (7+ years): Strategic engineer capable of leading teams and complex, cross-functional initiatives."
        ),
        PositivePillarCharacteristic(
            description="Senior+ – Focus on Who and When: Considers team composition, long-term ownership, sequencing of work, and organizational impact."
        ),
        PositivePillarCharacteristic(
            description="Senior+ – Challenges Assumptions: Respectfully reframes questions to maximize impact and alignment with business goals."
        ),
        PositivePillarCharacteristic(
            description="Senior+ – Strategic & Mentoring Mindset: Demonstrates ownership beyond technical delivery, focusing on team and business success."
        ),
        PositivePillarCharacteristic(
            description="Senior+ – Theory Handling: Uses questions as teaching moments, simplifying complex concepts with deep mastery."
        ),
        PositivePillarCharacteristic(
            description="Senior+ – Open-Ended Questions: Elevates discussions to include risks, operational costs, team skills, and long-term strategy."
        ),
        PositivePillarCharacteristic(
            description="Senior+ – Coding Approach: Focuses on architectural patterns and principles, discussing generalization and long-term precedents."
        ),
        PositivePillarCharacteristic(
            description="Senior+ – Technical Expertise: Very high; often a go-to expert in one or more domains."
        ),
        PositivePillarCharacteristic(
            description="Senior+ – Critical Thinking: Exceptional strategic and product-oriented reasoning."
        ),
        PositivePillarCharacteristic(
            description="Senior+ – Business Acumen: Thinks like a business owner and translates seamlessly between technical and business strategy."
        ),
        PositivePillarCharacteristic(
            description="Senior+ – Communication: Highly influential communicator who aligns and persuades stakeholders at all levels."
        ),
    ],
)

]
