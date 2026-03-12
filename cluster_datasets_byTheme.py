#!/usr/bin/env python3

import json
import sys

from grade8_themes import grade8_themes
from grade11_themes import grade11_themes


def match_themes(dataset_text, theme_dict):
    """
    Returns list of themes that match keywords in dataset_text.
    """
    matched = []

    for theme, keywords in theme_dict.items():
        for kw in keywords:
            if kw.lower() in dataset_text:
                matched.append(theme)
                break

    return matched


def main():

    if len(sys.argv) != 3:
        print("Usage: python3 cluster_datasets_by_theme.py input.json output.json")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r", encoding="utf-8") as f:
        datasets = json.load(f)

    clustered = []

    for ds in datasets:

        title = ds.get("title", "")
        excerpt = ds.get("excerpt", "")
        tags = ds.get("tags", [])
        topics = ds.get("topics", [])

        dataset_text = " ".join([
            title,
            excerpt,
            " ".join(tags),
            " ".join(topics)
        ]).lower()

        grade8_matches = match_themes(dataset_text, grade8_themes)
        grade11_matches = match_themes(dataset_text, grade11_themes)

        ds_result = {
            "title": title,
            "tags": tags,
            "topics": topics,
            "grade8_themes": grade8_matches,
            "grade11_themes": grade11_matches
        }

        clustered.append(ds_result)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(clustered, f, indent=2)

    print(f"Processed {len(clustered)} datasets.")
    print(f"Output written to: {output_file}")

    # -----------------------------
    # Theme → Dataset summary
    # -----------------------------

    from collections import defaultdict

    grade8_summary = defaultdict(list)
    grade11_summary = defaultdict(list)

    for ds in clustered:
        title = ds["title"]

        for theme in ds["grade8_themes"]:
            if len(grade8_summary[theme]) < 5: # prints out first 5 matching datasets, change if you want to see more
                grade8_summary[theme].append(title)

        for theme in ds["grade11_themes"]:
            if len(grade11_summary[theme]) < 5: # as above
                grade11_summary[theme].append(title)

    print("\nGRADE 8 THEMES → DATASETS")
    print("-------------------------")

    for theme, titles in grade8_summary.items():
        print(f"\n{theme}")
        for t in titles:
            print(f"  - {t}")

    print("\nGRADE 11 THEMES → DATASETS")
    print("--------------------------")

    for theme, titles in grade11_summary.items():
        print(f"\n{theme}")
        for t in titles:
            print(f"  - {t}")


if __name__ == "__main__":
    main()
