from selene import have
from demoqa_tests.pages.registration_page import RegistrationPage


def test_student_registration_form(setup_browser):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    (
        registration_page.fill_first_name('Olga')
        .fill_last_name('YA')
        .fill_email('name@example.com')
        .choose_gender('Female')
        .fill_phone_number('1234567891')
        .fill_date_of_birth('1999', 'May', '11')
        .choose_subject('Computer Science')
        .choose_hobby('Reading')
        .upload_photo('reference.png')
        .fill_address('Moscowskaya Street 18')
        .choose_state('NCR')
        .choose_city('Delhi')
        .click_submit_button('#submit')
    )
    # THEN
    registration_page.registered_user_data.should(
        have.exact_texts(
            'Olga YA',
            'name@example.com',
            'Female',
            '1234567891',
            '11 May,1999',
            'Computer Science',
            'Reading',
            'reference.png',
            'Moscowskaya Street 18',
            'NCR Delhi',
        )
    )
