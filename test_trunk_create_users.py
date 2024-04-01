import re
from playwright.sync_api import Page, expect
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://trunk-mysql8.nightly.sakaiproject.org/")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("admin")
    page.get_by_placeholder("Username").press("Tab")
    page.get_by_placeholder("Password").fill("admin")
    page.get_by_placeholder("Password").press("Enter")
    page.get_by_role("link", name="Users").click()
    # try closing the on-board dialogue
    #try:
    #    page.get_by_role("button", name="").click()
    #    page.get_by_role("link", name="Okay, got it!").click()
    #except:
    #    pass
    page.get_by_role("link", name="Import from file").click()
    page.get_by_role("button", name="Import a file").click()
    page.get_by_role("button", name="Add Add").click()
    # changing here
    page.get_by_role("link", name="Upload Files").click()
    with page.expect_file_chooser() as fc_info:
        page.get_by_role("button", name="Drop files to upload, or").click()
    file_chooser = fc_info.value
    file_chooser.set_files("users.csv")
    #page.get_by_role("button", name="Drop files to upload, or").click()
    #page.waitForEvent('filechooser')
    #page.get_by_role("button", name="Drop files to upload, or").set_input_files("wasi_25_users_CSV.csv")
    page.get_by_role("button", name="Continue").click()
    # count all links with select
    #page.get_by_role('Select').all()[-1].click()
    page.get_by_role("link", name="Select").last.click()
    page.locator("#attachButton1").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Profile image").click()
    page.get_by_role("link", name=" Log Out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
