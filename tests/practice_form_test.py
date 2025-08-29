from demoqa_tests.data.user import kos
from demoqa_tests.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.user_registration(kos)

    # THEN
    registration_page.registered_user_should_have_data(kos)
