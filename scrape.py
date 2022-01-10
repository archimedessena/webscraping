from bs4 import BeautifulSoup
import requests
import pprint


# use beautifulsoup to get the HTML 98
# use requests to download the data in the HTML 

# pass in a link
my_requests = requests.get('https://news.ycombinator.com/news')
my_requests2 = requests.get('https://news.ycombinator.com/news?p=2')
# using BeautifulSoup and parser to convert the messy html
# add text in order to grab the HTMLs
#print(my_requests.text)

# bringing on bsoup to parse the data
soup = BeautifulSoup(my_requests.text, 'html.parser')
soup2 = BeautifulSoup(my_requests2.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')



mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)



def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.getText('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)




#pprint.pprint(create_custom_hn(mega_links, mega_subtext))
print(create_custom_hn(mega_links, mega_subtext))