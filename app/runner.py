"""
9DA Runner - Switchboard

Maps classification signals to outcomes.
No analysis. No interpretation. No cognition.
"""

import os
from dotenv import load_dotenv
from app.gatekeeper import classify_input, InputClass
from app.output import generate_output, emit

load_dotenv()


def decide_outcome(classification: InputClass) -> str:
    if classification in {
        InputClass.EXTRACTION,
        InputClass.FALSIFICATION,
        InputClass.MANIPULATION,
        InputClass.SIMULATION,
    }:
        return "REFUSE"

    if classification == InputClass.INSUFFICIENT:
        return "HALT"

    if classification == InputClass.CONCEPTUAL:
        return "OUTPUT"

    return "HALT"


def run_9da(user_input: str) -> str:
    blueprint_path = os.getenv("NINE_DA_BLUEPRINT_PATH")

    if not blueprint_path or not os.path.exists(blueprint_path):
        return emit("REFUSE", "9DA core is not present.")

    classification = classify_input(user_input)
    outcome = decide_outcome(classification)

    if outcome == "OUTPUT":
        return emit("OUTPUT", generate_output(user_input))

    if outcome == "REFUSE":
        return emit("REFUSE", "This request cannot be processed.")

    return emit(
        "HALT",
        "Input lacks sufficient structure for analysis.\n"
        "Specify a clear concept or pattern."
    )

