import openpyxl
import os
import re

# Get user input for output file name and save the Excel sheet
output_name = input("Name of output file: ").strip()

# Check if the user included an extension. If not, append '.xlsx' to the filename
if not output_name.endswith('.txt'):
    output_name += '.txt'

path = r"C:\Users\Administrator\Documents\ParaDocsHealthPrototypes-main\ParaDocsHealthPrototypes-main\Output Files"

# Create the full path by joining the directory path and filename
full_path = os.path.join(path, output_name)


def extract_Plan(file_name):
    '''Extracts the section between "- Plan -" and "CPT � is a registered trademark of the American Medical Association".'''
    with open(file_name, 'r') as file:
        content = file.read()

    # Use regex to extract the desired section
    match = re.search(r'- Plan -\n\n(.*?)\n\nCPT', content, re.DOTALL)
    
    if match:
        return match.group(1).strip().split('\n')
    else:
        print("Desired section not found")
        return []



def main():
    # Get user input for file name
    file_name = input("Enter the path to the .txt file: ")

    # Extract section from text file
    Plan_data = extract_Plan(file_name)
    
      # Write the extracted data to a new text file
    with open(full_path, 'w') as output_file:
        output_file.write('\n'.join(Plan_data))
    
  
if __name__ == '__main__':
    main()
