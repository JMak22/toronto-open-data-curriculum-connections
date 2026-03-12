#!/usr/bin/env python3

import json
import sys
from pathlib import Path


def extract_display_names(tags):
    """
    From a CKAN-style tags list, keep only each tag's display_name.
    Returns a simple list of strings.
    """
    if not isinstance(tags, list):
        return []

    cleaned_tags = []
    for tag in tags:
        if isinstance(tag, dict):
            display_name = tag.get("display_name")
            if display_name:
                cleaned_tags.append(display_name)

    return cleaned_tags


def clean_dataset_record(record):
    """
    Keep only:
    - title
    - excerpt
    - topics
    - tags (display_name only)
    - formats
    """
    return {
        "title": record.get("title"),
        "excerpt": record.get("excerpt"),
        "topics": record.get("topics", []),
        "tags": extract_display_names(record.get("tags", [])),
        "formats": record.get("formats", []),
    }


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 trim_datasets.py input.json output.json")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f"Error: input file not found: {input_path}")
        sys.exit(1)

    try:
        with input_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: could not parse JSON: {e}")
        sys.exit(1)

    results = data.get("result", {}).get("results")
    if not isinstance(results, list):
        print("Error: expected data['result']['results'] to be a list.")
        sys.exit(1)

    cleaned_results = [clean_dataset_record(record) for record in results]

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(cleaned_results, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(cleaned_results)} cleaned dataset records to {output_path}")


if __name__ == "__main__":
    main()
