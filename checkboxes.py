import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless = False)
        context = await browser.new_context()
        await context.tracing.start(screenshots = True, snapshots = True, sources = True)
        page = await context.new_page()

        await page.goto("https://demoqa.com/checkbox")
        await page.check('label[for="tree-node-home"]')
        await page.screenshot(path='screenshots/checkboxes.png')
        await page.is_checked('label[for="tree-node-home"]') is True
        await expect(page.locator("#result")).to_have_text("You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFilexcelFile")
        await context.tracing.stop(path = "logs/trace.zip")
        await browser.close()

asyncio.run(main())