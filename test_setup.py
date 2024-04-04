from playwright.sync_api import Playwright, sync_playwright, expect
from utils.read_csv import get_user_list

users_list = get_user_list()
COURSE_NAME = "some4"

def test_login_admin(playwright: Playwright) -> None:
    global page, context, browser
    browser = playwright.chromium.launch(headless=False, slow_mo= 1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://trunk-mysql8.nightly.sakaiproject.org/")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("renee4")
    page.get_by_placeholder("Username").press("Tab")
    page.get_by_placeholder("Password").fill("sakai")
    page.get_by_placeholder("Password").press("Enter")


def test_add_users(playwright: Playwright) -> None:
    onboard_dialogue = page.get_by_text("Sakai is a flexible learning")
    if onboard_dialogue.count() > 0:
        page.get_by_role("button", name=" Click to dismiss").click()
        page.get_by_role("link", name="Okay, got it!").click()
    page.get_by_role("link", name="Users").click()
    page.get_by_role("link", name="Import from file").click()
    page.get_by_role("button", name="Import a file").click()
    page.get_by_role("button", name="Add Add").click()

    page.get_by_role("link", name="Upload Files").click()
    with page.expect_file_chooser() as fc_info:
        page.get_by_role("button", name="Drop files to upload, or").click()
    file_chooser = fc_info.value
    file_chooser.set_files("users.csv")
    page.get_by_role("button", name="Continue").click()
    #following always selects the most recent file uploaded
    page.get_by_role("link", name="Select").last.click()
    page.locator("#attachButton1").click()
    page.get_by_role("button", name="Continue").click()

def test_logout(playwright: Playwright) -> None:
    page.get_by_role("button", name="Profile image").click()
    page.get_by_role("link", name=" Log Out").click()

    # ---------------------
    #context.close()
    #browser.close()

def test_login_instructor(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo = 500)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://trunk-mysql8.nightly.sakaiproject.org/")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("renee")
    page.get_by_placeholder("Username").press("Tab")
    page.get_by_placeholder("Password").fill("sakai")
    page.get_by_placeholder("Password").press("Enter")

    # start creating course
    page.get_by_title("Open the view all sites").click()
    page.get_by_role("link", name="Create New Site").click()
    page.get_by_role("button", name="Continue").click()
    #page.goto("https://qa23-mysql8.nightly.sakaiproject.org/portal/site/%7Erenee/tool/da28a705-cd2f-4072-bd37-35f24efc867f?panel=Main")
    # first login
    try:
        #page.goto("https://qa23-mysql8.nightly.sakaiproject.org/portal/site/%7Erenee/tool/da28a705-cd2f-4072-bd37-
        page.get_by_role("button", name="Continue").click()
    except:
        pass
    page.get_by_role("link", name="Still cannot find your course").click()

    page.get_by_label("Subject:").click()
    page.get_by_label("Subject:").fill(COURSE_NAME)
    page.get_by_label("Subject:").press("Tab")
    page.get_by_label("Course:").fill("1")
    page.get_by_label("Course:").fill("1")
    page.get_by_label("Course:").press("Tab")
    page.get_by_label("Section:").fill("1")
    page.get_by_label("* Authorizer's username:").click()

    page.get_by_label("* Authorizer's username:").fill("admin")
    page.get_by_label("* Authorizer's username:").fill("admin")
    page.get_by_role("button", name="Continue").click()

    page.frame_locator("iframe[title=\"Editor\\, description\"]").locator("html").click()
    page.frame_locator("iframe[title=\"Editor\\, description\"]").get_by_label("Editor, description").fill("This is a sample course site. ")
    page.get_by_role("button", name="Continue").click()
    # adding tools
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

    page.get_by_label("Source").click()
    page.get_by_label("Source").fill("http://yahoo.com")
    page.get_by_role("button", name="Continue").click()

    page.get_by_label("Manual", exact=True).check()
    page.get_by_label("Published - immediately").check()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Request Site").click()

    # start adding participants
    #page.get_by_role("button", name="Expand tool list").click()
    page.locator("#siteList").get_by_role("link", name="%s 1 1 Spring"%COURSE_NAME).click()
    page.get_by_role("link", name="Site Info").click()
    page.get_by_role("link", name="Add Participants").click()
    page.get_by_label("Official Email Address or").click()
    page.get_by_label("Official Email Address or").fill(users_list)
    #page.get_by_label("Official Email Address or").fill("tawest\ntonorth\ntoeast\ntosouth\nrenee2\nrenee3\nrenee4\nrenee5\nrenee6\nrenee7\nrenee9\nrenee10\nrenee11\nrenee12\nrenee13\nrenee14\nrenee16\nrenee15\ntawest1\ntonorth1\ntoeast1\ntosouth1")
    page.get_by_role("button", name="Continue").click()
    page.get_by_label("Student").check()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Finish").click()

    # logout as instructor
    page.get_by_role("button", name="Profile image").click()
    page.get_by_role("link", name=" Log Out").click()

    context.close()
    browser.close()


