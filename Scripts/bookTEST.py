
#https://www.youtube.com/watch?v=E4wU8y7r1Uc
#https://www.youtube.com/watch?v=DqXVfRkY-WA


from playwright.sync_api import sync_playwright, Playwright
import json

def run(playwright: Playwright):
    start_url = "https://books.toscrape.com/"
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(start_url)
    #page.click('article.product_pod h3 a');

    pageNUM = page.locator('ul.pager li.current')

    print(pageNUM);

    while True: 
        for link in page.locator('article.product_pod h3 a').all()[:1]:
            p = browser.new_page(base_url=start_url)
            url = link.get_attribute("href")
            if url is not None:
                p.goto(url)
            else:
                p.close()
            
            data = p.locator('h1.book-title')

            #print(data)

            p.close()
    
    
        data = page.locator('ul.pager li.next a')
        url = data.get_attribute("href")
        url = url.replace('catalogue/',"")
        
        print(url)
        page.goto(start_url+'catalogue/'+url)

        
      
   

def scrape_quotes(playwright: Playwright):
    start_url = "https://quotes.toscrape.com/"
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto(start_url)

    quotes = page.locator('.text').all_text_contents()
    for quote in quotes:
        print(quote)

    browser.close()

def meow(playwright: Playwright):
    start_url = "https://news.ycombinator.com/newest"
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(start_url)
    #page.click('article.product_pod h3 a');

    pageNUM = page.locator('span.subline span.age')
    print(pageNUM)


with sync_playwright() as playwright:
    run(playwright)