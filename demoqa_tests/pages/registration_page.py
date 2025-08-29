from selene import browser, have, command
from demoqa_tests import resource


class RegistrationPage:

    # def __init__(self):
    #     self.registered_user_data = browser.element('.table').all('td').even

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(2)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def choose_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def choose_subject(self, name):
        browser.element('#subjectsInput').type(name).press_enter()
        return self

    def choose_hobby(self, name):
        browser.all('.custom-checkbox').element_by(have.exact_text(name)).perform(
            command.js.scroll_into_view
        ).click()
        return self

    def upload_photo(self, file):
        browser.element('#uploadPicture').set_value(resource.path(file))
        return self

    def fill_address(self, name):
        browser.element('#currentAddress').type(name)
        return self

    def choose_state(self, name):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def choose_city(self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def click_submit_button(self, name):
        browser.element(name).perform(command.js.click)

    # Аннотация @property используется, чтобы вызвать метод без аргументов (см. ниже), не используя скобки - registered_user_data
    @property
    def registered_user_data(self):
        return browser.element('.table').all('td').even

    # def should_have_registered_user_with(
    #     self,
    #     first_name,
    #     last_name,
    #     email,
    #     gender,
    #     phone_number,
    #     date_of_birth,
    #     subject,
    #     hobby,
    #     photo,
    #     address,
    #     state,
    #     city
    # ):
    #     browser.element('.table').all('td').even.should(
    #         have.exact_texts(
    #             f'{first_name} {last_name}',
    #             email,
    #             gender,
    #             phone_number,
    #             date_of_birth,
    #             subject,
    #             hobby,
    #             photo,
    #             address,
    #             f'{state} {city}'
    #         )
    #     )
