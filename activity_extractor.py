import re
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ACTIVITIES_FILE = BASE_DIR / "data" / "activities.json"

with open(ACTIVITIES_FILE, "r", encoding="utf-8") as file:
    ACTIVITIES = json.load(file)

# ==========================================================
# Text Cleaning
# ==========================================================

def clean_text(text):
    """
    Normalize journal text for keyword matching.
    """

    text = text.lower()

    # Replace punctuation with spaces
    text = re.sub(r"[^\w\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ==========================================================
# Activity Extraction
# ==========================================================

def extract_activities(journal):
    """
    Extract activities mentioned in a journal.

    Returns a list of activity objects sorted by confidence.
    """

    journal = clean_text(journal)

    activities_found = []

    for activity, keywords in ACTIVITIES.items():

        frequency = 0
        matched_keywords = []

        for keyword in set(keywords):

            keyword = keyword.lower()

            # Match complete words/phrases only
            pattern = re.compile(
                r"\b" + re.escape(keyword) + r"\b"
            )

            matches = pattern.findall(journal)

            if matches:

                frequency += len(matches)
                matched_keywords.append(keyword)

        if frequency > 0:

            confidence = round(
                min(frequency / 5, 1.0),
                2
            )

            activities_found.append({

                "activity": activity,

                "keywords": matched_keywords,

                "frequency": frequency,

                "confidence": confidence

            })

    activities_found.sort(
        key=lambda activity: activity["confidence"],
        reverse=True
    )

    return activities_found


# ==========================================================
# Demo
# ==========================================================

if __name__ == "__main__":

    journal = """
    Today I completed my FastAPI backend.

    Later I practiced volleyball.

    Then I read a machine learning book.

    Finally I wrote more Python code.
    """

    activities = extract_activities(journal)

    print("\nDetected Activities\n")

    for activity in activities:

        print(f"Activity   : {activity['activity']}")
        print(f"Keywords   : {activity['keywords']}")
        print(f"Frequency  : {activity['frequency']}")
        print(f"Confidence : {activity['confidence']}")
        print("-" * 40)