import asyncio
from playwright.async_api import async_playwright, expect
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless= False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources= True)
        page = await context.new_page()
        await  page.goto("https://demoqa.com/buttons")
        button = page.locator("text = Click Me").nth(2)
        await button.click()
        await page.screenshot(path = "screnshots/dynamicClick.png")
        await expect(page.locator("#dynamicClickMessage")).to_have_text("You have done a dynamic click")
        button = page.locator(("text = Click Me")).nth(0)
        await button.dblclick()
        await page.screenshot(path = 'screenshots/doubleClick.png')
        await expect(page.locator("#doubleClickMessage")).to_have_text("You have done a double click")
        await context.tracing.stop(path = "logs/trace.zip")
        await browser.close()
asyncio.run(main())