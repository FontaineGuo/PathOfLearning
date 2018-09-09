from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
                    
    def page_links(self):
        return self.links

    def error(self, message):
        pass


# the crawler can't simply find out relative link 
# for example, if the website address is 'www.fontianeguo.com'
# you could write some links without typeing 'www.fontaineguo.com'
# eg. 'www.fontaineguo.com/video_56.html' -> '/video_56.html'