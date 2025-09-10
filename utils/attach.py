import allure
import requests
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name='screenshot',
        attachment_type=AttachmentType.PNG,
        extension='.png',
    )


# Не работает, так как в селеноиде нет метода get_log
# def add_logs(browser):
#     log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
#     allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_logs(browser):
    session_id = browser.driver.session_id
    selenoid_url = "https://selenoid.autotests.cloud"  # без /wd/hub
    log_url = f"{selenoid_url}/logs/{session_id}.log"

    response = requests.get(
        log_url, auth=("user1", "1234")
    )
    if response.status_code == 200:
        allure.attach(
            response.text, name="browser_logs", attachment_type=AttachmentType.TEXT
        )
    else:
        allure.attach(
            f"Не удалось получить логи. Код ответа: {response.status_code}",
            name="browser_logs",
            attachment_type=AttachmentType.TEXT,
        )


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = (
        "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    )
    html = (
        "<html><body><video width='100%' height='100%' controls autoplay><source src='"
        + video_url
        + "' type='video/mp4'></video></body></html>"
    )
    allure.attach(
        html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html'
    )
