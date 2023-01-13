from selenium import webdriver
import random

def search_youtube(query, k):
    # Open the Chrome browser
    global driver
    driver = webdriver.Chrome()

    # Navigate to YouTube and search for the query
    driver.get("https://www.youtube.com/")
    search_bar = driver.find_element("name", "search_query")
    search_bar.send_keys(query)
    search_bar.submit()

    # Extract the video links from the search results
    video_links = []
    video_elements = driver.find_elements('xpath', "//a[contains(@href,'watch')]")
    for video in video_elements:
        video_links.append(video.get_attribute("href"))

    # Choose k random videos from the search results
    random_video_links = random.sample(video_links, k)

    # Open each video in a new tab
    for link in random_video_links:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(link)


query = input('Enter a search term: ')
k = int(input('Enter the number of videos to return: '))
search_youtube(query, k)
