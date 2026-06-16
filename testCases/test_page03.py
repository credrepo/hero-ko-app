import pytest
from Pages.Page03 import Page03


@pytest.mark.usefixtures("setup")
class Test_Pagethree:

    def test_verity_all_test(self, setup):
        p3 = Page03(setup)

        p3.click_element()
        p3.click_checkbox()
        p3.click_home()
        p3.click_homelist()
        p3.click_desktop()
