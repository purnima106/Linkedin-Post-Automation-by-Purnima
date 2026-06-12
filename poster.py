# pyrefly: ignore [missing-import]
from groq.types.chat import chat_completion_assistant_message_param
# pyrefly: ignore [missing-import]
from playwright.sync_api import sync_playwright


def post_to_linkedin(post_text):

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            context = browser.new_context(
                storage_state="linkedin_session.json"
            )

            page = context.new_page()

            page.goto(
                "https://www.linkedin.com/feed/"
            )

            page.wait_for_timeout(5000)

            print("URL:", page.url)
            print("TITLE:", page.title())

            page.screenshot(path="linkedin_debug.png")

            try:
                print(page.content()[:2000])
            except Exception as e:
                print("Could not print page content:", e)

            page.locator(
                '[aria-label="Start a post"]'
            ).click()

            page.wait_for_timeout(3000)

            page.keyboard.type(
                post_text,
                delay=20
            )

            page.wait_for_timeout(2000)

            page.get_by_role(
                "button",
                name="Post",
                exact=True
            ).click()
            # print("Ready to click Post")

            # input("Press Enter to publish...")

            page.wait_for_timeout(5000)

            browser.close()

            return True

    except Exception as e:

        print(e)

        return False

if __name__ == "__main__":
    post_to_linkedin(
        """
Testing LinkedIn automation.

This post was inserted automatically using Playwright.

#AI #DevOps
"""
    )

# from linkedin_api import Linkedin
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def get_client():

#     email = os.getenv("LINKEDIN_EMAIL")
#     password = os.getenv("LINKEDIN_PASSWORD")

#     return Linkedin(email, password)
