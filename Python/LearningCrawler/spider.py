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
        Spider.quene_file = Spider.project_name + '/quene.txt' 
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

