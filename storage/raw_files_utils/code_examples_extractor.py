import requests
import json
import os

def fetch_ipynb_from_github(github_url):
    """
    Fetch the content of a .ipynb file from a given GitHub URL.
    """
    raw_url = github_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    response = requests.get(raw_url)
    response.raise_for_status()
    return response.text

def process_and_collect_content(github_url):
    """
    Process a single GitHub URL to fetch a .ipynb or .py file and convert it to Markdown. 
    Return the markdown content.
    """
    try:
        file_content = fetch_ipynb_from_github(github_url)
        if ".ipynb" in github_url:
            markdown_content = convert_ipynb_to_md(file_content)
        elif ".py" in github_url:
            # Wrap the Python file content in a Markdown code block
            markdown_content = "```python\n" + file_content + "\n```\n"
        else:
            raise ValueError(f"Unsupported file type in URL: {github_url}")
        
        print(f"Processed {github_url}")
        return markdown_content
    except Exception as e:
        print(f"Error processing {github_url}: {e}")
        return ""

def convert_ipynb_to_md(ipynb_content):
    """
    Convert the content of a .ipynb file to Markdown format, excluding output cells.
    """
    notebook = json.loads(ipynb_content)
    markdown_content = ""

    for cell in notebook['cells']:
        cell_type = cell['cell_type']

        if cell_type == 'markdown' or cell_type == 'raw':
            markdown_content += "\n".join(cell['source']) + "\n\n"
        elif cell_type == 'code':
            markdown_content += "```python\n" + "".join(cell['source']) + "\n```\n"

    return markdown_content

def save_to_md_file(filename, content):
    """
    Save the provided content to a .md file with the given filename.
    """
    with open(filename, 'w') as file:
        file.write(content)

def main_single_output(url_list, output_filename):
    """
    Process a list of GitHub URLs and save the combined content to a single .md file.
    """
    combined_markdown_content = ""

    for github_url in url_list:
        combined_markdown_content += process_and_collect_content(github_url)
        combined_markdown_content += "\n\n---\n\n"  # Add a separator between notebooks

    save_to_md_file(output_filename, combined_markdown_content)
    print(f"Combined Markdown content saved to {output_filename}")

# Example usage:
urls = [
    "https://github.com/EdgeCaser/Snapshotsurfer/blob/master/Snapshot%20Surfer%202%20-%20Olympus%20Edition.ipynb",
    "https://github.com/EdgeCaser/Snapshotsurfer/blob/master/Snapshot%20Surfer%202.ipynb",
    "https://github.com/EdgeCaser/Snapshotsurfer/blob/master/Snapshotdiver.py",
    "https://github.com/EdgeCaser/Snapshotsurfer/blob/master/Snapshotsurfer%20Web.py",
    "https://github.com/EdgeCaser/Snapshotsurfer/blob/master/Snapshotsurfer.ipynb",
    "https://github.com/EdgeCaser/Snapshotsurfer/blob/master/Snapshotsurfer.py",
]
main_single_output(urls, "subgrounds_code_examples_vanilla_apis.md")

