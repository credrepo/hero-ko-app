import pytest
from Pages.Page04 import Page04


@pytest.mark.usefixtures("setup")
class Test_Pagefour:

    def test_verity_all_test(self, setup):
        p4 = Page04(setup)

        p4.click_buttons()
