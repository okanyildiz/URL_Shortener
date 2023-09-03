import requests
import re

def shorten_url(url):
    response = requests.get(f'http://tinyurl.com/api-create.php?url={url}')
    if response.status_code == 200:
        return response.text
    else:
        return None

def main():
    with open('input.md', 'r') as infile, open('output.md', 'w') as outfile:
        content = infile.read()
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
        count=0
        for url in urls:
            count+=1
            print(count)
            short_url = shorten_url(url.replace(")",""))
            if short_url:
                content = content.replace(url.replace(")",""), short_url)
        outfile.write(content)

if __name__ == '__main__':
    print('Powered by Okan YILDIZ')
    main()