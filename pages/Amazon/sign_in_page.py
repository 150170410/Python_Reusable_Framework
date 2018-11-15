class SignInPage():

    def __init__(self, logger, webdriver, base_page):
        self.saveto = logger
        self.bp = base_page
        self.driver = webdriver

    # Locators
    email_text_field_xpath = "//input[@name='email']"
    password_text_field_xpath = "//input[@name='password']"
    continue_button_class = "a-button-input"


    # Constants


    # Functions
    def login_with_email_password(self, email, password):
        self.bp.enter_value_in_text_field_by_xpath(self.email_text_field_xpath, email)
        self.bp.element_click_by_class(self.continue_button_class)
        self.bp.enter_value_in_text_field_by_xpath(self.password_text_field_xpath, password)
        self.bp.element_click_by_class(self.continue_button_class)
