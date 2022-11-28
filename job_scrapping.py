from bs4 import BeautifulSoup
import requests
import time

## for timesjobs
def find_job():
    print("Please choose your location and skills!")
    # city = input("Location: ")
    familiar_skill = input("Familiar skill: ")

    html_text =requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').text
        
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
            exp_and_location = job.find('ul', class_ = 'top-jd-dtl clearfix')

## years of experience and location 
            for i in exp_and_location.find_all('i', class_ = 'material-icons'):
                i.decompose()
                exp_year = exp_and_location.find('li').text
                location = exp_and_location.find('span').text
                
            if 'Bengaluru' not in location:
                skills = job.find('span', class_ = 'srp-skills').text.strip().replace('  ',' ')
                more_info = job.header.h2.a['href']
                
## familiar skill               
                if familiar_skill in skills:
                    with open(f'posts/{index}.txt', 'w') as f:
                        f.write(f'Company Name: {company_name}')
                        f.write(f'Experience: {exp_year} \nLocation: {location}\nSkills: {skills}\n')
                        f.write(f'More info: {more_info} \n')
                    print(f'File saved {index}')

if __name__ == '__main__':
    # while True:
    #     find_job()
    #     time.sleep(60*1000)
    find_job()