from urllib.request import urlopen
from link_finder import LinkFinder
from general import *



class Spider:
    
    # Class variables(shared among all instances)
    project_name = ''
    base_url = ''
    domin_name = ''
    quene_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domin_name = domain_name
        Spider.quene_file = Spider.project_name + '/queue.txt' 
        Spider.crawled_file = Spider.project_name + '/crawled.txt' 
        self.boot()
        self.crawl_page('First spider', Spider.base_url)  


    # class method using self, depend function or methond don't need self
    @staticmethod
    def boot():
         create_project_dir(Spider.project_name)
         create_data_files(Spider.project_name, Spider.base_url)
         Spider.quene = file_to_set(Spider.quene_file)
         Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + '  | crawled: '
                                            + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()
        
    @staticmethod
    def gather_link(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domin_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.quene_file)
        set_to_file(Spider.crawled, Spider.crawled_file)