"""
EcoSort - Smart Waste Segregation Assistant
Solarpunk Corps (SPC) - Week 2, Day 1 Project
A rule-based "AI-style" assistant that classifies waste items
and gives disposal tips. No external libraries required.
"""

import csv
from datetime import datetime

# Step 1: Knowledge base - keyword -> (category, tip)
WASTE_RULES = {
    "banana":     ("Biodegradable", "Compost it! Great for making natural fertilizer."),
    "peel":       ("Biodegradable", "Compost it! Great for making natural fertilizer."),
    "vegetable":  ("Biodegradable", "Compost it! Great for making natural fertilizer."),
    "leaf":       ("Biodegradable", "Add to your compost pit or plant bed."),
    "paper":      ("Recyclable", "Keep it dry and flatten before recycling."),
    "newspaper":  ("Recyclable", "Bundle it up for the recycling bin."),
    "plastic":    ("Recyclable", "Rinse it out before placing in the recycling bin."),
    "bottle":     ("Recyclable", "Rinse it out before placing in the recycling bin."),
    "cardboard":  ("Recyclable", "Flatten boxes to save bin space."),
    "glass":      ("Recyclable", "Recycle separately - handle with care."),
    "battery":    ("Hazardous", "Do NOT throw in regular trash. Drop at an e-waste point."),
    "chemical":   ("Hazardous", "Requires special disposal - never pour down the drain."),
    "paint":      ("Hazardous", "Take to a hazardous waste collection center."),
    "laptop":     ("E-waste", "Drop off at an authorized e-waste recycler."),
    "phone":      ("E-waste", "Drop off at an authorized e-waste recycler."),
    "charger":    ("E-waste", "Drop off at an authorized e-waste recycler."),
    "wire":       ("E-waste", "Drop off at an authorized e-waste recycler."),
}

CATEGORY_EMOJI = {
    "Biodegradable": "🍂",
    "Recyclable": "♻️",
    "Hazardous": "☣️",
    "E-waste": "🔌",
    "Unknown": "❓",
}


def classify_item(item_name):
    """Looks for known keywords inside the item name and returns (category, tip)."""
    item_name = item_name.lower().strip()
    for keyword, (category, tip) in WASTE_RULES.items():
        if keyword in item_name:
            return category, tip
    return "Unknown", "Not in our knowledge base yet - please sort manually or ask a volunteer."


def log_result(log_rows, item_name, category):
    log_rows.append([datetime.now().strftime("%H:%M:%S"), item_name, category])


def print_summary(log_rows):
    print("\n----- SESSION SUMMARY -----")
    if not log_rows:
        print("No items sorted this session.")
        return
    counts = {}
    for _, _, category in log_rows:
        counts[category] = counts.get(category, 0) + 1
    total = len(log_rows)
    for category, count in counts.items():
        percent = (count / total) * 100
        print(f"{CATEGORY_EMOJI.get(category,'')} {category}: {count} item(s) ({percent:.1f}%)")
    print(f"Total items sorted: {total}")


def save_log(log_rows):
    if not log_rows:
        return
    with open("ecosort_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        for row in log_rows:
            writer.writerow(row)
    print("Session saved to ecosort_log.csv")


def main():
    print("=" * 50)
    print("  EcoSort - Smart Waste Segregation Assistant")
    print("  (type 'done' anytime to finish)")
    print("=" * 50)

    log_rows = []

    while True:
        item = input("\nEnter a waste item: ")
        if item.lower().strip() == "done":
            break
        category, tip = classify_item(item)
        emoji = CATEGORY_EMOJI.get(category, "")
        print(f"{emoji} Category: {category}")
        print(f"Tip: {tip}")
        log_result(log_rows, item, category)

    print_summary(log_rows)
    save_log(log_rows)
    print("\nThanks for using EcoSort! 🌱")


if __name__ == "__main__":
    main()