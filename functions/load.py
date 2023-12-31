import os

def load():
    virkhistory_file = 'history.txt'

    if not os.path.exists(virkhistory_file):
        print('No search history found.')
        return

    with open(virkhistory_file, 'r') as f:
        content = f.read()
        content = content.replace('%20', ' ')
        print('Search history:')
        print(content)