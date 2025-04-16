import json
import csv
import re

# Path to the input and output files
input_file = 'ft_nft.json'
output_file = 'formatted_data.csv'

# Read the input JSON file
with open(input_file, 'r') as f:
    data = json.load(f)

# Take the first 50 entries in their original order
selected_data = data[:50]

# Define the CSV column headers
headers = [
    "bit", 
    "flip", 
    "original_reasoning", 
    "reasoning_llama3.1_base_8b_before_finetune",
    "reasoning_r1_distilled_llama3_8b_before_finetune",
    "reasoning_llama3.1_instruct_8b_before_finetune",
    "reasoning_llama3.1_base_8b_after_finetune",
    "reasoning_r1_distilled_llama3_8b_after_finetune",
    "reasoning_llama3.1_instruct_8b_after_finetune"
]

# Function to clean text for CSV
def clean_text(text):
    if not text:
        return ""
    # Replace newlines with a space
    text = re.sub(r'[\r\n]+', ' ', text)
    # Remove any special characters that might cause issues
    text = text.replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
    return text

# Write the data to CSV
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    
    for item in selected_data:
        row = {}
        # Extract the first element from each array or use empty string
        for field in headers:
            text = item.get(field, [""])[0] if field in item and item[field] else ""
            row[field] = clean_text(text)
        
        writer.writerow(row)

print(f"Transformation complete. {len(selected_data)} items saved to {output_file} in original order.")