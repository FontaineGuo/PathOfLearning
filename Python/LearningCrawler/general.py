import os 

# each website you crawl is a separate project(folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project' + directory)
        os.mkdir(directory)


# create quene file and crawled files (if not created)
def create_data_files(project_name, base_url):
    quene = project_name + '/quene.txt'
    crawled = project_name + '/crawled.txt'

    if not os.path.isfile(quene):
        write_file(quene, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')  

# create a new file 
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close() 

# add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass

# read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# iterate through a set, each iteam wii be a new line in a file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
