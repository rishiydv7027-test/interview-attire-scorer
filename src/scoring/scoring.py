"""
Step 7: Scoring Logic
--------------------------
Purpose: Convert classifier results (tucked/untucked, formal/casual shoes,
beard groomed/not, etc.) into a single weighted score from 0-100.

TODO:
- Define weight for each attribute (e.g. shirt_tuck: 25%, shoes: 20%, etc.)
- Map each classifier output to a numeric sub-score
- Combine sub-scores into a final weighted score
"""

ATTRIBUTE_WEIGHTS = {
    "shirt_tuck": 0.25,
    "beard": 0.15,
    "hair": 0.15,
    "shoes": 0.25,
    "pants": 0.20,
}


def calculate_score(classifier_results):
    """Convert classifier results dict into a final 0-100 score. Placeholder."""
    pass
