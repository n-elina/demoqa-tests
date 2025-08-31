import allure
import json
from allure import attachment_type
from allure_commons.types import Severity
from demoqa_tests.data.user import kos
from demoqa_tests.pages.registration_page import RegistrationPage


def test_student_registration_form():
    with allure.step('Открываем страницу регистрации'):
        registration_page = RegistrationPage()
        registration_page.open()

    # WHEN
    with allure.step('Регистрация пользователя Kos'):
        registration_page.user_registration(kos)

    # THEN
    with allure.step(
        'Проверяем, что пользователь Kos зарегистрировался с корректными данными'
    ):
        registration_page.registered_user_should_have_data(kos)


registration_page = RegistrationPage()


def test_student_registration_with_decorator_steps():
    open_registration_page()
    registration_user_Kos()
    user_Kos_should_have_data()


@allure.step('Открываем страницу регистрации')
def open_registration_page():
    registration_page.open()


@allure.step('Регистрация пользователя Kos')
def registration_user_Kos():
    registration_page.user_registration(kos)


@allure.step('Проверяем, что пользователь Kos зарегистрировался с корректными данными')
def user_Kos_should_have_data():
    registration_page.registered_user_should_have_data(kos)


def test_attachments():
    allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)
    allure.attach(
        "<h1>Hello, world</h1>", name="Html", attachment_type=attachment_type.HTML
    )
    allure.attach(
        json.dumps({"first": 1, "second": 2}),
        name="Json",
        attachment_type=attachment_type.JSON,
    )


def test_no_labels():
    pass


def test_dynamic_labels():
    # Разметка больше для программирования, например, с уловием if...
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story(
        "Неавторизованный пользователь не может создать задачу в репозитории"
    )
    allure.dynamic.link("https://github.com", name="Testing")
    pass


# Более правильная разметка
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    pass
