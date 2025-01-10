import json
import os

# Get the current working directory
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# Read the JSON payload file from the same directory
json_file_path = r"D:\Admin Python Practice\python-for-devops\Day-02\examples\string-replace.json"  # Use raw string (r) for Windows paths

# Read the JSON payload file
with open(json_file_path, "r") as file:  # Pass the variable, not the string
    data = json.load(file)  # Load JSON data as a dictionary

# Extract the text from the JSON
text = data.get("text", "")  # Default to an empty string if 'text' key is not found

# Perform the string replace operation
new_text = text.replace("awesome", "damn easy")

# Print the modified text
print("Modified text:", new_text)

# Optionally, update the JSON payload with the new text
data["text"] = new_text

# Save the updated JSON back to the file
with open(json_file_path, "w") as file:  # Pass the variable, not the string
    json.dump(data, file, indent=4)
