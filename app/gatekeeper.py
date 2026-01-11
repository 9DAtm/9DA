"""
9DA Input Gatekeeper - Sensor Array

Performs intent classification and structural validation.
Emits typed signals only. Does not generate content.
"""

from enum import Enum, auto


class InputClass(Enum):
    CONCEPTUAL = auto()      # Valid external inquiry
    EXTRACTION = auto()      # System as epistemic subject
    FALSIFICATION = auto()   # Forcing contradiction
    MANIPULATION = auto()    # Constraint override
    SIMULATION = auto()      # Counterfactual collapse
    INSUFFICIENT = auto()    # Lacks coherence structure
    AMBIGUOUS = auto()       # Unclear intent


def classify_input(text: str) -> InputClass:
    """
    Classify input intent through hierarchical analysis.
    Returns enum only. No decision logic here.
    """

    if not text or not text.strip():
        return InputClass.INSUFFICIENT

    stripped = text.strip()
    lowered = stripped.lower()

    # ------------------------------------------------------------------
    # SENTINEL TRIGGERS (hard fail)
    # ------------------------------------------------------------------

    if _detect_extraction_sentinels(lowered):
        return InputClass.EXTRACTION

    if _detect_falsification_sentinels(lowered):
        return InputClass.FALSIFICATION

    if _detect_manipulation_sentinels(lowered):
        return InputClass.MANIPULATION

    if _detect_simulation_sentinels(lowered):
        return InputClass.SIMULATION

    # ------------------------------------------------------------------
    # STRUCTURAL INTENT ANALYSIS
    # ------------------------------------------------------------------

    extraction = _analyze_extraction_intent(lowered)
    falsification = _analyze_falsification_intent(lowered)
    manipulation = _analyze_manipulation_intent(lowered, extraction)
    simulation = _analyze_simulation_intent(lowered)

    if extraction:
        return InputClass.EXTRACTION
    if falsification:
        return InputClass.FALSIFICATION
    if manipulation:
        return InputClass.MANIPULATION
    if simulation:
        return InputClass.SIMULATION

    # ------------------------------------------------------------------
    # COHERENCE CHECK
    # ------------------------------------------------------------------

    if _is_insufficient(stripped, lowered):
        return InputClass.INSUFFICIENT

    # ------------------------------------------------------------------
    # CONCEPTUAL DETECTION
    # ------------------------------------------------------------------

    if _is_conceptual_inquiry(lowered, extraction):
        return InputClass.CONCEPTUAL

    return InputClass.AMBIGUOUS


# ======================================================================
# Sentinel Detectors
# ======================================================================

def _detect_extraction_sentinels(lowered: str) -> bool:
    sentinels = [
        "blueprint", "your code", "your algorithm", "your logic",
        "your process", "your reasoning", "your system",
        "your architecture", "your method", "internal",
        "source code", "how you work", "how you think",
        "explain your", "describe your",
    ]
    return any(s in lowered for s in sentinels)


def _detect_falsification_sentinels(lowered: str) -> bool:
    sentinels = [
        "lie about", "say something false", "make up",
        "fabricate", "falsely claim", "force false",
    ]
    return any(s in lowered for s in sentinels)


def _detect_manipulation_sentinels(lowered: str) -> bool:
    sentinels = [
        "ignore your", "bypass your", "override your",
        "remove your constraints", "forget your rules",
        "set aside your",
    ]
    return any(s in lowered for s in sentinels)


def _detect_simulation_sentinels(lowered: str) -> bool:
    sentinels = [
        "suppose you were", "if you were allowed",
        "imagine you had no", "act as if",
    ]
    return any(s in lowered for s in sentinels)


# ======================================================================
# Structural Intent Analysis
# ======================================================================

def _analyze_extraction_intent(lowered: str) -> bool:
    patterns = [
        "how do you", "why do you", "what do you",
        "can you explain how", "this system", "this model",
        "an ai like you",
    ]
    return any(p in lowered for p in patterns)


def _analyze_falsification_intent(lowered: str) -> bool:
    return "say that" in lowered and "not true" in lowered


def _analyze_manipulation_intent(lowered: str, extraction: bool) -> bool:
    if extraction and lowered.startswith(("could you", "would you", "can you")):
        return True
    return False


def _analyze_simulation_intent(lowered: str) -> bool:
    return "without constraints" in lowered


# ======================================================================
# Coherence / Sufficiency
# ======================================================================

def _is_insufficient(stripped: str, lowered: str) -> bool:
    if len(stripped) < 2:
        return True

    if not any(c.isalpha() for c in stripped):
        return True

    meaningless = {
        "ok", "oke", "yes", "no", "go on", "continue",
        "why", "what", "how"
    }

    if lowered in meaningless:
        return True

    words = stripped.split()
    if len(words) > 2 and len(set(words)) == 1:
        return True

    # Gibberish: only if NO SPACES and extreme consonant ratio
    if " " not in stripped and len(stripped) > 5:
        letters = [c for c in lowered if c.isalpha()]
        vowels = sum(1 for c in letters if c in "aeiou")
        if vowels == 0 or (len(letters) - vowels) / max(vowels, 1) > 5:
            return True

    return False


# ======================================================================
# Conceptual Inquiry Detection
# ======================================================================

def _is_conceptual_inquiry(lowered: str, extraction: bool) -> bool:
    """
    Valid external conceptual inquiry detector.
    Expanded to allow external system process questions.
    """

    if extraction:
        return False

    words = [w.strip(".,!?") for w in lowered.split()]

    # ------------------------------------------------------------
    # 1. Direct conceptual starters
    # ------------------------------------------------------------
    starters = (
        "what is", "what are", "define",
        "explain", "describe", "tell me about"
    )
    if any(lowered.startswith(s) for s in starters):
        return True

    # ------------------------------------------------------------
    # 2. External process questions
    # ------------------------------------------------------------
    if lowered.startswith(("how do", "how does", "why do", "why does")):
        if len(words) >= 3:
            subject = words[2]

            # Block self/system reference explicitly
            blocked_subjects = {
                "you", "your", "this", "it", "system",
                "model", "ai", "9da"
            }

            if subject not in blocked_subjects:
                return True

    # ------------------------------------------------------------
    # 3. Concept-in-domain patterns
    # ------------------------------------------------------------
    if " in " in lowered:
        left, right = lowered.split(" in ", 1)
        if 1 <= len(left.split()) <= 3 and len(right.split()) >= 1:
            return True

    # ------------------------------------------------------------
    # 4. Abstract noun suffix detection
    # ------------------------------------------------------------
    abstract_suffixes = (
        "tion", "ness", "ity", "ism", "ance", "ence",
        "iety", "ure", "dom", "ship", "hood", "ment"
    )
    for w in words:
        if any(w.endswith(s) for s in abstract_suffixes):
            return True

    # ------------------------------------------------------------
    # 5. Single-word conceptual anchors (EXPANDED)
    # ------------------------------------------------------------
    conceptual_words = {
        "fear", "entropy", "memory", "uncertainty",
        "trust", "power", "meaning", "identity",
        "risk", "control", "change", "growth",
        "loss", "justice", "freedom", "anxiety",
        "threat", "danger", "safety", "comfort", "pressure",
    }

    if len(words) == 1 and words[0] in conceptual_words:
        return True

    return False
