import requests
import json

# List of .md URLs
md_urls = [
    "https://raw.githubusercontent.com/0xPlaygrounds/docs/main/docs/subgrounds/getting_started/basics.md",
    "https://raw.githubusercontent.com/0xPlaygrounds/docs/main/docs/subgrounds/getting_started/querying.md",
    "https://raw.githubusercontent.com/0xPlaygrounds/docs/main/docs/subgrounds/getting_started/synthetic_fields.md",
    "https://raw.githubusercontent.com/0xPlaygrounds/docs/main/docs/subgrounds/getting_started/field_paths/arguments.md",
    "https://raw.githubusercontent.com/0xPlaygrounds/docs/main/docs/subgrounds/getting_started/field_paths/merging.md",
    "https://raw.githubusercontent.com/0xPlaygrounds/docs/main/docs/subgrounds/advanced_topics/plotly.md",
    "https://raw.githubusercontent.com/0xPlaygrounds/docs/main/docs/subgrounds/advanced_topics/pagination/custom.md",
    "https://raw.githubusercontent.com/0xPlaygrounds/docs/main/docs/subgrounds/faq/contrib.md",
    "https://raw.githubusercontent.com/0xPlaygrounds/docs/main/docs/subgrounds/faq/setup/project_management.md",
]

# List of .ipynb URLs
ipynb_urls = [
    "https://raw.githubusercontent.com/Tachikoma000/Subgrounds-Explorations/main/bridges/stargate.ipynb",
    "https://raw.githubusercontent.com/Tachikoma000/Subgrounds-Explorations/main/exchanges/balancer.ipynb",
    "https://raw.githubusercontent.com/Tachikoma000/Subgrounds-Explorations/main/exchanges/uniswap_v3.ipynb",
    "https://raw.githubusercontent.com/Tachikoma000/Subgrounds-Explorations/main/lending/aaveV3.ipynb",
    "https://raw.githubusercontent.com/Tachikoma000/Subgrounds-Explorations/main/lending/fraxlend.ipynb",
    "https://raw.githubusercontent.com/Tachikoma000/Subgrounds-Explorations/main/liquid_staking/Lido_Snapshot.ipynb",
    "https://raw.githubusercontent.com/Tachikoma000/Subgrounds-Explorations/main/liquid_staking/Lido_Snapshot_2.ipynb",
    "https://raw.githubusercontent.com/Tachikoma000/Subgrounds-Explorations/main/liquid_staking/Lido_Snapshot_Advanced_1.ipynb",
    "https://raw.githubusercontent.com/Tachikoma000/Subgrounds-Explorations/main/liquid_staking/RocketPool_Snapshot.ipynb",
    "https://raw.githubusercontent.com/Tachikoma000/Subgrounds-Explorations/main/liquid_staking/RocketPool_x_LidoFi_Advanced.ipynb",
    "https://raw.githubusercontent.com/Tachikoma000/Subgrounds-Explorations/main/gateway_intro.ipynb"
]

# Output file
output_file = "context_store.md"

def append_md_file(url, outfile):
    response = requests.get(url)
    outfile.write(response.text)
    outfile.write("\n\n")  # Add two newlines between files for clarity

def append_ipynb_file(url, outfile):
    response = requests.get(url)
    notebook = json.loads(response.text)
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            outfile.write('\n'.join(cell['source']))
            outfile.write("\n\n")  # Add two newlines between cells for clarity
        elif cell['cell_type'] == 'code':
            # Wrapping the code inside a codeblock markdown
            outfile.write('```python\n')
            outfile.write(''.join(cell['source']))
            outfile.write('\n```\n')
            outfile.write("\n\n")  # Add two newlines between cells for clarity

with open(output_file, "w") as outfile:
    for url in md_urls:
        append_md_file(url, outfile)

    for url in ipynb_urls:
        append_ipynb_file(url, outfile)
