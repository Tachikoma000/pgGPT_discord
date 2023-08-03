import requests
from bs4 import BeautifulSoup
import html2text

def scrape_and_convert_to_md(url_list, output_filename):
    # Instantiate HTML2Text
    h = html2text.HTML2Text()
    h.ignore_links = False

    # Open the file in append mode, so data isn't overwritten for each site
    with open(output_filename, 'a', encoding='utf-8') as f:
        for url in url_list:
            # Send a request to the webpage
            response = requests.get(url)
            # Make sure the request was successful
            if response.status_code != 200:
                print(f"Failed to get webpage: {url}")
                continue

            # Parse the webpage's content
            soup = BeautifulSoup(response.content, 'html.parser')
            html_content = str(soup.prettify())

            # Convert HTML to Markdown and write to the file
            markdown_content = h.handle(html_content)
            f.write(markdown_content + "\n\n")

# Example usage
url_list = ['https://docs.playgrounds.network/subgrounds/api/subgrounds/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.pagination/',  
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.pagination.preprocess/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.pagination.strategies/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.pagination.utils/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.subgraph/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.subgraph.fieldpath/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.subgraph.filter/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.subgraph.object/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.subgraph.subgraph/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.client/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.dash_wrappers/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.dataframe_utils/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.plotly_wrappers/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.query/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.schema/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.subgrounds/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.transform/',
            'https://docs.playgrounds.network/subgrounds/api/subgrounds.utils/',
            'https://docs.playgrounds.network/api/api-reference/',
            'https://docs.playgrounds.network/api/reference/proxy/',
            'https://docs.playgrounds.network/api/reference/proxy/subgraph_id/',
            'https://docs.playgrounds.network/api/reference/proxy/deployment_id/']  # replace with your list of urls
output_filename = 'output.md'  # replace with your desired output filename
scrape_and_convert_to_md(url_list, output_filename)
