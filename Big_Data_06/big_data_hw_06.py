from bs4 import BeautifulSoup
import os
import requests


url = 'https://www.taiwanstat.com/waters/latest'
response = requests.get(url)
response_json = response.json()[0]
response_html = "<table border='1'>"
response_html += '\n<tr><th>水庫<th/><th>蓄水量<th/></tr>'

str = 'baseAvailable'

for key in response_json:
    response_html += f'\n\t<tr><th>{key}<th/><th>{response_json[key][str]}萬立方公尺<th/></tr>'

response_html += '\n<table/>'

with open('respose.html', 'w+', encoding='utf-8') as f:
    f.write(response_html)

# ------------------------------------------------------

phoneNos = "0212345678, 02 66571234, 02-2911-5637, " +  \
    "(02) 66571256, (02)66571278, (02)6657-1290, " +  \
    "(02) 6657-1298, (02) 6657 1299"

remove_char_lst = ['(', ')', '-', ' ']
for i in remove_char_lst:
    phoneNos = phoneNos.replace(i, '')

phoneNosList = phoneNos.split(',')
for phonenum in phoneNosList:
    print(f'({phonenum[:2]}) {phonenum[2:6]}-{phonenum[6:]}')

# ------------------------------------------------------

def render_image(image):
    response = requests.get(image)
    return(response.content)

def create_image_to_folder(folder, image, index):
    with open(f'{folder}/images{index}.jpg', 'wb') as f:
        f.write(render_image(image))

def create_images_to_folder(folder, images):
    for index, image in enumerate(images):
        try:
            create_image_to_folder(folder, image["src"], index)
        except:
            pass    

def catch_image(url):

    response = requests.get(url)

    images= BeautifulSoup(response.content, "html.parser").find_all("img")
    
    try:
        os.makedirs("images")
        create_images_to_folder('images', images)
    except:
        pass

url = "https://www.4gamers.com.tw/news/detail/57200/detective-conan-movie-special-movie-2023-march"
catch_image(url)
