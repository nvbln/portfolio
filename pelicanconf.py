import os
import yaml

PATH = "content"

def load_files(file_dir):
    file_dir = PATH + "/" + file_dir
    all_file_data = []
    for filename in reversed(os.listdir(file_dir)):
        if filename.endswith(".yml"):
            with open(os.path.join(file_dir, filename), 'r') as f:
                data = yaml.safe_load(f)
                all_file_data.append(data)
    return all_file_data

JINJA_GLOBALS = {
    'project_summaries': load_files("project_summaries"),
    'education': load_files("education")
}

AUTHOR = 'Firstname Lastname'
SITENAME = 'Firstname Portfolio'
SITEURL = ""

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (
#    ("Pelican", "https://getpelican.com/"),
#    ("Python.org", "https://www.python.org/"),
#    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#    ("You can modify those links in your config file", "#"),
#)

# Social widget
#SOCIAL = (
#    ("You can add links in your config file", "#"),
#    ("Another social link", "#"),
#)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARCHIVES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
