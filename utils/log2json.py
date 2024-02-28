import re
from collections import defaultdict
import json


def normal_log2json():
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


def log2json():
    with open("../system.log", "r") as file:
        log_content = file.read()

    # Define patterns to identify stack traces and method calls
    stack_trace_pattern = r"(ERROR|WARN|FATAL)"
    method_pattern = r"\s(\w+\.java) \(line \d+\)|\tat (\w+\.java):\d+"

    # Split the log content into lines
    log_lines = log_content.split("\n")

    # Initialize lists to store nodes and relations
    nodes = []
    relations = []
    processed_methods = set()
    previous_method = None
    in_stack_trace = False  # To keep track of whether we're inside a stack trace

    # Iterate over the log lines to extract methods and build relations
    for line in log_lines:
        is_stack_trace = re.search(stack_trace_pattern, line)
        method_match = re.search(method_pattern, line)

        if is_stack_trace:
            in_stack_trace = True

        # If the line contains a method call
        if method_match:
            method = method_match.group(1) if method_match.group(1) else method_match.group(2)
            suspicion_value = 0.7 if in_stack_trace else 0.3  # Set suspicion based on context

            # Append method to nodes if not already processed
            if method not in processed_methods:
                nodes.append({"id": method, "suspicion": suspicion_value})
                processed_methods.add(method)

            # Build relation if there was a previous method in the sequence
            if previous_method:
                relations.append({"from": previous_method, "to": method})

            previous_method = method

        # Reset the stack trace flag if line is empty (assuming stack traces are separated by empty lines)
        if not line.strip():
            in_stack_trace = False

    # Create the final JSON structure
    json_structure_final = {
        "nodes": nodes,
        "relations": relations
    }
    file_path = "../input.json"
    with open(file_path, "w") as json_file:
        json.dump(json_structure_final, json_file, indent=4)



if __name__ == "__main__":
    log2json()
