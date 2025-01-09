import yaml  # Import the yaml module

# Create a dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Machine Learning", "Web Development"]
}

# Write the dictionary to a YAML file
with open("data.yaml", "w") as yaml_file:                 # Opens a file named data.yaml in write ("w") mode
    yaml.dump(data, yaml_file, default_flow_style=False)  # Converts the dictionary to YAML and writes it to the file , 'default_flow_style=False' ensures the YAML is written in a block format, which is more human-readable.

print("Dictionary written to data.yaml")