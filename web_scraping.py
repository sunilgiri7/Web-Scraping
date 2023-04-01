import requests
from bs4 import BeautifulSoup
import time

print("Put some skills that your are not familiar with")
unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills}....')

def find_jobs():
    html_text = requests.get('https://www.placementindia.com/job-search/python-developer-fresher-jobs-in-pune.htm').text
    soup = BeautifulSoup(html_text, 'html.parser')
    job = soup.find_all('div', class_='sjci')

    for index, jobs in enumerate(job):
        job_role = jobs.find('a', class_='job-name')
        if job_role is not None:
            job_role = job_role.text
        else:
            continue
        if 'Developer' in job_role:
            skills = jobs.find('div', class_='sk_list').text
            location = jobs.find('ul', class_='sjci-need').li.text
            more_info = jobs.h2.a['href']

            if unfamiliar_skills not in skills:
                with open(f'post {index}.txt', 'w') as f:
                    f.write(f'Job Role: {job_role.strip()} \n')
                    f.write(f'Skills: {skills.strip()} \n')
                    f.write(f'Experience : {location.strip()} \n')
                    f.write(f'More Info : {more_info}')
                print(f'File saved {index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_weight = 10
        print(f'waiting {time_weight} minutes to exit or press ctrl c....')
        time.sleep(60 * time_weight)