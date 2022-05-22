import requests, bs4
from helpers import *

choice = get_topic()
print('\nGetting latest article links from %s...' % (choice))

article_list = extract_links(f'https://medium.com/topic/{choice}')
print(f'Total articles found: {len(article_list)}')

for i in range(len(article_list)):
    heading = article_list[i].getText()
    artlink = article_list[i].get('href')
    artlink = (
        artlink
        if artlink.startswith("https://")
        else f"https://medium.com{artlink}"
    )

    print(f'Downloading article: {str(i+1)}')

    # remove invalid characters from filename
    file_name = f"{heading}.txt".replace(':', '').replace('?', '')
    with open(file_name, 'w') as file:
        article_text = medium_text(artlink)
        file.write(article_text)
print('Done.')