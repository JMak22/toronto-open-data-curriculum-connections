# What's this?

A small exploratory project looking at connections between:

- Ontario Grade 8 Geography curriculum (2023)
- Ontario Grade 11 Introduction to Spatial Technologies curriculum (2015)
- datasets available through the City of Toronto Open Data portal

The goal was to see how Toronto Open Data datasets could be grouped around classroom inquiry themes.

This is **not a finished product**, just a quick experiment to explore possibilities.

# Methodology

1. Keywords were extracted from the Overall Expectations for both courses.
2. Keywords were then grouped into thematic dictionaries for each grade.
3. A Python script scanned the Toronto Open Data dataset metadata (title, excerpt, tags, and topics).
4. Case-insensitive keyword matching was used to identify datasets that might align with each theme. (care was taken not to look for a "best" match as one dataset could fit into any number of class inquiry topics, depending on teacher and student interest)

The dataset metadata was downloaded from the Toronto Open Data API on March 12, 2026 and trimmed to the fields most relevant to discovery:

- title  
- excerpt  
- topics  
- tags  
- formats  

# Repository contents

- grade8_themes.py - keyword dictionary
- grade11_themes.py - keyword dictionary
- toronto_datasets_trimmed.json - simplified dataset metadata used for the analysis
- cluster_datasets_by_theme.py - scans the dataset metadata and creates connections with the keyword dictionaries

# Running the script

```python3 cluster_datasets_by_theme.py toronto_datasets_trimmed.json clustered_datasets.json```

The script outputs:
- a JSON file showing which themes each dataset matches
- a short console summary of example datasets for each theme

# Caveats

This is intentionally lightweight. Keyword matching is simple substring matching, no machine learning or semantic analysis was used.
The goal was illustration, not precision. 

# Now what?

Go forth and find the perfect dataset for your class inquiry, or that one student who won't stop asking questions about busses, traffic lights, fire stations or what ever they're interested in.

