from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('C:/Users/user/Downloads/chromedriver')

file = open('JoJo_part_4_links.html', 'w+')

driver.get(
    "https://www18.gogoanime.io/category/jojo-no-kimyou-na-bouken-diamond-wa-kudakenai-dub")
wait = WebDriverWait(driver, 400)
wait.until(EC.presence_of_element_located((By.ID, 'episode_related')))
anchors = driver.find_element_by_id('episode_related').find_elements_by_tag_name('a')
episode_links = list()
for anchor in anchors:
    episode_links.append(anchor.get_attribute('href'))

for episode_link in episode_links[:5]:
    driver.get(episode_link)
    download_link = driver.find_element_by_class_name('anime_video_body_cate')
    download_link = driver.find_element_by_link_text('Download').get_attribute('href')

    driver.get(download_link)
    episode_name = driver.find_element_by_class_name('name').text
    d_links = driver.find_elements_by_class_name('dowload')
    file.write('<h3>{}</h3><br>'.format(episode_name))
    for d_link in d_links:
        a = d_link.find_element_by_tag_name('a')
        file.write(('<a href = {}>{}</a><br>'.format(a.get_attribute('href'), a.text)))

file.close()
print('all done')
