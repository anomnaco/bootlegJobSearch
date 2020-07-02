from bs4 import BeautifulSoup
import re
import readtime
import json
import requests

#25 per page
page = requests.get('https://www.monster.com/jobs/search/?q=cassandra&intcid=skr_navigation_nhpso_searchMain')
bs = BeautifulSoup(page.content, 'html.parser')
results = bs.findAll('a', attrs={'href': re.compile("^https://")})
result_links = [result.get('href') for result in results]
#print(result_links)
rl_copy = result_links.copy()
for i in range(len(result_links)):
    if not 'job-openings' in result_links[i]:
        rl_copy.remove(result_links[i])

#print(rl_copy)

new_page = BeautifulSoup(requests.get('https://job-openings.monster.com/10-exp-java-backend-developer-sunnyvale-ca-locals-only-sunnyvale-ca-us-kutir-technologies/218500582').content, 'html.parser')
print(new_page.find("div", {"class": "full-jobview-container page-container"}))
