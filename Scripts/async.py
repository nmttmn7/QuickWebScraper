import asyncio
from playwright.async_api import async_playwright
#https://www.youtube.com/watch?v=a3HJnbYhXUc
url = 'https://www.example.com'

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        print(await page.title())
        await browser.close()

asyncio.run(main())