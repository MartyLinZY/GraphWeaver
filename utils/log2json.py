import re
from collections import defaultdict
import json

with open("../system.log", "r") as file:
    log_content = file.read()

# Initialize lists to store nodes and relations
nodes = []
relations = []
processed_methods = set()
method_relations = defaultdict(list)

# Regular expression pattern to extract method calls from log
pattern = r"\s(\w+\.java) \(line \d+\)"

# Find all method calls in the log content
matches = re.findall(pattern, log_content)

# Process each match
for i in range(len(matches)):
    method = matches[i]
    if method not in processed_methods:
        nodes.append({"id": method, "suspicion": 0.5})  # Add to nodes with default suspicion
        processed_methods.add(method)
    if i < len(matches) - 1:
        # Create a relation between the current method and the next one
        relations.append({"from": method, "to": matches[i + 1]})
        method_relations[method].append(matches[i + 1])

# Create the final JSON structure
json_structure = {
    "nodes": nodes,
    "relations": relations
}

print(json_structure)

file_path = "../input.json"
with open(file_path, "w") as json_file:
    json.dump(json_structure, json_file, indent=4)