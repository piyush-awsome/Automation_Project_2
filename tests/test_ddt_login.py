import pytest

from pages.login_page import LoginPage

from utilities.excel_utils import *


file = "ddt_login_data.xlsx"


@pytest.mark.parametrize(
    "row",
    range(2, get_row_count(file, "LoginData") + 1)
)

def test_login_ddt(setup, row):

    driver = setup

    login = LoginPage(driver)

    email = read_data(file, "LoginData", row, 1)

    password = read_data(file, "LoginData", row, 2)

    login.enter_email(email)

    login.enter_password(password)

    login.click_login()

    if row == 5:

        assert login.login_successful()

    else:

        assert not login.login_successful()