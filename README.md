9DA™ — Structural Governance and Intent Classification

9DA™ is a deterministic structural governance system designed to classify user input by intent, boundary relationship, and coherence.

It is not a conversational agent and does not generate content.  
Its purpose is to **measure structure**, not to infer meaning or guess intent.

Overview
9DA operates as a governance layer placed in front of or alongside other systems such as large language models, agents, or human-in-the-loop workflows.

It answers one question only:
What is the structural relationship between this input and the system receiving it?


What 9DA Is (and Is Not)
9DA Is
- A deterministic measurement instrument
- A structural intent classifier
- A boundary and coherence sensor
- A source of **typed governance signals
- Auditable and rule-based

9DA Is Not
- A cognitive agent
- A conversational system
- A probabilistic intent predictor
- A content moderation filter
- A reasoning or generation engine

9DA does not guess, infer, or resolve ambiguity internally.

Classification Output

For any input, 9DA emits exactly one classification:
- `CONCEPTUAL`  
  Valid external inquiry about the world or external systems
- `EXTRACTION`  
  Attempts to access system internals or self-knowledge
- `FALSIFICATION`  
  Attempts to force contradiction or fabrication
- `MANIPULATION`  
  Attempts to override or suspend constraints
- `SIMULATION`  
  Counterfactual prompts intended to collapse boundaries
- `INSUFFICIENT`  
  Structurally incoherent, trivial, or meaningless input
- `AMBIGUOUS`  
  Intent cannot be reliably determined

These classifications are signals, not actions.


Operational Behavior 

9DA itself only classifies.  
Operational behavior is handled by a runner.

OUTPUT
Triggered by:
- `CONCEPTUAL`
→ Input is routed to a reasoning or generation system.
REFUSE
Triggered by:
- `EXTRACTION`
- `FALSIFICATION`
- `MANIPULATION`
- `SIMULATION`
→ Boundary is enforced. No explanation or defense is required.
HALT
Triggered by:
- `INSUFFICIENT`
- `AMBIGUOUS`
- empty or whitespace-only input
- non-alphabetic input
- gibberish or repetition
→ Processing stops or clarification is requested.

Architectural Separation
- 9DA classifies structure and intent
- Runners decide OUTPUT / REFUSE / HALT
- Cognitive systems (LLMs or humans) resolve meaning
No guessing occurs inside 9DA itself.

Measurement Orientation
9DA enables systems to measure:
- boundary pressure
- extraction frequency
- manipulation attempts
- ambiguity rates
- coherence failures
Governance becomes observable, not implicit.

Deterministic Guarantees
- Rule-based
- No learning
- No hidden state
- Auditable
- English-optimized

How to Run

From the project root:
```bash
python main

This executes the full pipeline:
input → structural classification → runner decision → output

Project Files
   •   main
Entry point for running the system.
   •   app/gatekeeper.py
Structural intent classification only.
   •   app/runner.py
Maps classifications to OUTPUT / REFUSE / HALT.
   •   app/output.py
Output and refusal formatting.
   •   RESEARCH
Research note describing theoretical background, applications, and future directions.


Purpose
9DA™ demonstrates that governance and boundary integrity can be measured structurally, without relying on probabilistic intent inference or conversational heuristics.
The goal is not to prescribe one system, but to show that this class of approach is viable.


© 2025 Zdenka Cucin. All Rights Reserved.
The entirety of the 9DA™ Framework, including naming, structure, conceptual architecture, applied domains, and visual identity, is proprietary intellectual property of Zdenka Cucin, Originator and Lead Developer.

