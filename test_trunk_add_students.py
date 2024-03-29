import re
from playwright.sync_api import Page, expect
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://trunk-mysql8.nightly.sakaiproject.org/")
    page.get_by_text("jump to content [c] Sites [w] Tools [l] Welcome View System Alert Username").click()
    page.frame_locator("iframe[title=\"Home Information Message\"]").get_by_role("heading", name="Welcome to Sakai").click()
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("renee")
    page.get_by_placeholder("Username").press("Tab")
    page.get_by_placeholder("Password").fill("sakai")
    page.get_by_placeholder("Password").press("Enter")
    page.get_by_role("button", name="Expand tool list").click()
    page.get_by_role("link", name="Site Info").click()
    page.get_by_role("link", name="Add Participants").click()
    page.get_by_label("Official Email Address or").click()
    page.get_by_label("Official Email Address or").fill("tawest\ntonorth\ntoeast\ntosouth\nrenee2\nrenee3\nrenee4\nrenee5\nrenee6\nrenee7\nrenee9\nrenee10\nrenee11\nrenee12\nrenee13\nrenee14\nrenee16\nrenee15\ntawest1\ntonorth1\ntoeast1\ntosouth1")
    page.get_by_role("button", name="Continue").click()
    page.get_by_label("Student").check()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Finish").click()
    page.get_by_role("link", name=" Log Out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)