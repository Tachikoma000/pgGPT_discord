def merge_md_files(input_file1, input_file2, output_file):
    with open(input_file1, 'r') as file1, open(input_file2, 'r') as file2, open(output_file, 'w') as outfile:
        outfile.write(file1.read())
        outfile.write("\n\n")  # Ensure there's a newline between contents
        outfile.write(file2.read())

# Example usage
file1 = 'playgrounds_docs_with_code_cleaned.md'  # replace with your first input filename
file2 = 'subgrounds_code_examples_vanilla_apis.md'  # replace with your second input filename
output_file = 'merged_raw_docs.md'  # replace with your desired output filename

merge_md_files(file1, file2, output_file)
