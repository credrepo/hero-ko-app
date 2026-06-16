import pytest
from Pages.Page01 import Page01

@pytest.mark.skip
@pytest.mark.usefixtures("setup")
class Test_Pageone:

    def test_verify_title(self):
        p1 = Page01(self.driver)
        p1.element_page()
        p1.text_box_button()
        p1.enter_full_name()
        p1.enter_email()
        p1.enter_address()
        p1.enter_perm_add()
        p1.click_button_submit()