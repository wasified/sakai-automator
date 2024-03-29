import re
from playwright.sync_api import Page, expect
import time

##def test_has_title(page: Page):
##    page.goto("https://playwright.dev/")
##
##    # Expect a title "to contain" a substring.
##    expect(page).to_have_title(re.compile("Playwright"))
##
##def test_get_started_link(page: Page):
##    page.goto("https://playwright.dev/")
##
##    # Click the get started link.
##    page.get_by_role("link", name="Get started").click()
##
##    # Expects page to have a heading with the name of Installation.
##    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


from playwright.sync_api import Playwright, sync_playwright, expect


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://qa23-mysql8.nightly.sakaiproject.org/")
    page.get_by_placeholder("Username").click()
    time.sleep(2)
    page.get_by_placeholder("Username").fill("renee")
    page.get_by_placeholder("Username").press("Tab")
    page.get_by_placeholder("Password").fill("sakai")
    page.get_by_placeholder("Password").press("Enter")
    page.get_by_title("Open the view all sites").click()
    page.get_by_role("link", name="Create New Site").click()
    page.get_by_role("button", name="Continue").click()
    #page.goto("https://qa23-mysql8.nightly.sakaiproject.org/portal/site/%7Erenee/tool/da28a705-cd2f-4072-bd37-35f24efc867f?panel=Main")
    # first login
    try:
        #page.goto("https://qa23-mysql8.nightly.sakaiproject.org/portal/site/%7Erenee/tool/da28a705-cd2f-4072-bd37-
        page.get_by_role("button", name="Continue").click()
        time.sleep(2)
    except:
        pass
    page.get_by_role("link", name="Still cannot find your course").click()
    time.sleep(2)
    page.get_by_label("Subject:").click()
    page.get_by_label("Subject:").fill("Vj101")
    page.get_by_label("Subject:").press("Tab")
    page.get_by_label("Course:").fill("1")
    page.get_by_label("Course:").press("CapsLock")
    page.get_by_label("Course:").fill("1")
    page.get_by_label("Course:").press("Tab")
    page.get_by_label("Section:").fill("1")
    page.get_by_label("* Authorizer's username:").click()
    time.sleep(2)
    page.get_by_label("* Authorizer's username:").fill("ADMIN")
    page.get_by_label("* Authorizer's username:").press("CapsLock")
    page.get_by_label("* Authorizer's username:").fill("admin")
    page.get_by_role("button", name="Continue").click()
    time.sleep(2)
    page.frame_locator("iframe[title=\"Editor\\, description\"]").locator("html").click()
    page.frame_locator("iframe[title=\"Editor\\, description\"]").get_by_label("Editor, description").fill("This is a sample course site. ")
    page.get_by_role("button", name="Continue").click()
    time.sleep(2)
    page.get_by_label("Assignments").check()
    page.get_by_label("Dashboard").check()
    page.get_by_label("Conversations").check()
    page.locator("#sakai_forums_wrap").click()
    page.get_by_label("Discussions").check()
    page.get_by_label("Drop Box").check()
    page.get_by_label("Email", exact=True).check()
    page.get_by_label("Calendar", exact=True).check()
    page.get_by_label("Chat Room").check()
    page.get_by_label("Commons").check()
    page.get_by_label("Contact Us").check()
    page.get_by_label("Gradebook").check()
    page.get_by_label("Email Archive").check()
    page.get_by_label("Lessons").check()
    page.get_by_label("Messages").check()
    page.get_by_label("News").check()
    page.get_by_label("Podcasts").check()
    page.get_by_label("Polls").check()
    page.get_by_label("PostEm").check()
    page.get_by_label("Resources").check()
    page.get_by_label("Roster").check()
    page.get_by_label("Rubrics").check()
    page.get_by_label("Search", exact=True).check()
    page.get_by_label("Section Info").check()
    page.get_by_label("Statistics").check()
    page.get_by_label("Sign-up").check()
    page.get_by_label("Syllabus").check()
    page.get_by_label("Tests & Quizzes").check()
    page.get_by_label("Web Content").check()
    page.get_by_label("Wiki").check()
    page.get_by_role("button", name="Continue").click()
    time.sleep(2)
    page.get_by_label("Source").click()
    page.get_by_label("Source").fill("http://yahoo.com")
    page.get_by_role("button", name="Continue").click()
    time.sleep(2)
    page.get_by_label("Manual", exact=True).check()
    page.get_by_label("Published - immediately").check()
    page.get_by_role("button", name="Continue").click()
    time.sleep(2)
    page.get_by_role("button", name="Request Site").click()
    time.sleep(2)
    page.get_by_role("link", name=" Log Out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
