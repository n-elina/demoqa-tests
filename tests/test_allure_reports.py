import allure
from allure_commons.types import Severity
from demoqa_tests.data.user import kos
from demoqa_tests.pages.registration_page import RegistrationPage
from tests.conftest import setup_browser


def test_student_registration_form(setup_browser):
    with allure.step('Открываем страницу регистрации'):
        registration_page = RegistrationPage(setup_browser)
        registration_page.open()

    # WHEN
    with allure.step('Регистрация пользователя Kos'):
        registration_page.user_registration(kos)

    # THEN
    with allure.step(
        'Проверяем, что пользователь Kos зарегистрировался с корректными данными'
    ):
        registration_page.registered_user_should_have_data(kos)


def test_student_registration_with_decorator_steps(setup_browser):
    open_registration_page(setup_browser)
    registration_user_Kos(setup_browser)
    user_Kos_should_have_data(setup_browser)


@allure.step('Открываем страницу регистрации')
def open_registration_page(browser):
    RegistrationPage(browser).open()


@allure.step('Регистрация пользователя Kos')
def registration_user_Kos(browser):
    RegistrationPage(browser).user_registration(kos)


@allure.step('Проверяем, что пользователь Kos зарегистрировался с корректными данными')
def user_Kos_should_have_data(browser):
    RegistrationPage(browser).registered_user_should_have_data(kos)


def test_no_labels():
    pass


def test_dynamic_labels():
    # Разметка больше для программирования, например, с условием if...
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
