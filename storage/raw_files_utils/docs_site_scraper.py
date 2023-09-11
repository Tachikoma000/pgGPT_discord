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
url_list = ['https://docs.playgrounds.network/subgrounds/',
            'https://docs.playgrounds.network/subgrounds/getting_started/',  
            'https://docs.playgrounds.network/subgrounds/getting_started/basics/',
            'https://docs.playgrounds.network/subgrounds/getting_started/field_paths/',
            'https://docs.playgrounds.network/subgrounds/getting_started/field_paths/arguments/',
            'https://docs.playgrounds.network/subgrounds/getting_started/field_paths/filtering/',
            'https://docs.playgrounds.network/subgrounds/getting_started/field_paths/sorting/',
            'https://docs.playgrounds.network/subgrounds/getting_started/field_paths/merging/',
            'https://docs.playgrounds.network/subgrounds/getting_started/querying/',
            'https://docs.playgrounds.network/subgrounds/getting_started/synthetic_fields/',
            'https://docs.playgrounds.network/subgrounds/advanced_topics/pagination/',
            'https://docs.playgrounds.network/subgrounds/advanced_topics/pagination/custom/',
            'https://docs.playgrounds.network/subgrounds/faq/more_data/',
            'https://docs.playgrounds.network/subgrounds/advanced_topics/contrib/plotly/',
            'https://docs.playgrounds.network/subgrounds/api_reference/top_level/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/client/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/contrib/plotly/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/contrib/dash/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/pagination/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/pagination/strategies/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/pagination/preprocess/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/pagination/pagination/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/pagination/utils/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/transform/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/subgraph/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/subgraph/fieldpath/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/query/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/utils/',
            'https://docs.playgrounds.network/subgrounds/api_reference/internal/schema/',
            'https://docs.playgrounds.network/api/',
            'https://docs.playgrounds.network/api/key/',
            'https://docs.playgrounds.network/api/subgraph-proxy/',
            'https://docs.playgrounds.network/api/subgrounds/',
            'https://docs.playgrounds.network/api/faq/query/',
            'https://docs.playgrounds.network/api/api-reference/',
            'https://docs.playgrounds.network/api/reference/proxy/',
            'https://docs.playgrounds.network/api/reference/proxy/subgraph_id/',
            'https://docs.playgrounds.network/api/reference/proxy/deployment_id/',]  # replace with your list of urls
output_filename = 'playgrounds_docs.md'  # replace with your desired output filename
scrape_and_convert_to_md(url_list, output_filename)
