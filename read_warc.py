from warcio.archiveiterator import ArchiveIterator
from bs4 import BeautifulSoup

# Open the WARC file we generated with Wget
with open('my_tiny_crawl.warc.gz', 'rb') as stream:
    for record in ArchiveIterator(stream):
        # We only care about HTTP responses (the actual downloaded HTML)
        if record.rec_type == 'response':
            content = record.content_stream().read()
            soup = BeautifulSoup(content, 'html.parser')
            
            # Extract and print the title
            if soup.title and soup.title.string:
                url = record.rec_headers.get_header('WARC-Target-URI')
                title = soup.title.string.strip()
                print(f"URL: {url}")
                print(f"Title: {title}\n")