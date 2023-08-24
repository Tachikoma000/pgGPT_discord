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
    Process a single GitHub URL to fetch a .ipynb file and convert it to Markdown. 
    Return the markdown content.
    """
    try:
        ipynb_content = fetch_ipynb_from_github(github_url)
        markdown_content = convert_ipynb_to_md(ipynb_content)
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
    "https://github.com/Tachikoma000/Subgrounds-Explorations/blob/main/bridges/stargate.ipynb",
    "https://github.com/Tachikoma000/Subgrounds-Explorations/blob/main/exchanges/balancer.ipynb",
    "https://github.com/Tachikoma000/Subgrounds-Explorations/blob/main/exchanges/bancor.ipynb",
    "https://github.com/Tachikoma000/Subgrounds-Explorations/blob/main/exchanges/uniswap_v3.ipynb",
    "https://github.com/Tachikoma000/Subgrounds-Explorations/blob/main/lending/aaveV3.ipynb",
    "https://github.com/Tachikoma000/Subgrounds-Explorations/blob/main/lending/fraxlend.ipynb",
    "https://github.com/Tachikoma000/Subgrounds-Explorations/blob/main/liquid_staking/Lido_Snapshot.ipynb",
    "https://github.com/Tachikoma000/Subgrounds-Explorations/blob/main/liquid_staking/Lido_Snapshot_2.ipynb",
    "https://github.com/Tachikoma000/Subgrounds-Explorations/blob/main/liquid_staking/Lido_Snapshot_Advanced_1.ipynb",
    "https://github.com/Tachikoma000/Subgrounds-Explorations/blob/main/liquid_staking/RocketPool_Snapshot.ipynb",
    "https://github.com/Tachikoma000/Subgrounds-Explorations/blob/main/liquid_staking/RocketPool_x_LidoFi_Advanced.ipynb",
    "https://github.com/Tachikoma000/Subgrounds-Explorations/blob/main/gateway_intro.ipynb",
]
main_single_output(urls, "subgrounds_code_examples.md")

