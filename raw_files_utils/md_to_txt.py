# Convert Markdown to Text
def md_to_txt(md_file_path, txt_file_path):
    # Read the content of the Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        content = md_file.read()

    # Write the content to a text file
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(content)

if __name__ == "__main__":
    source_md_file = input("Enter the path to the Markdown file: ")
    target_txt_file = input("Enter the path for the output text file: ")

    md_to_txt(source_md_file, target_txt_file)
    print(f"Converted {source_md_file} to {target_txt_file} successfully!")