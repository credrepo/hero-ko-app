import pytest
from Pages.Page05 import Page05


@pytest.mark.usefixtures("setup")
class Test_Pagefive:

    def test_verity_all_test(self, setup):
        p5 = Page05(setup)

        p5.click_widget_btn()       # direct URL pe jayega
        p5.click_date_picker()      # input click — calendar open
        p5.click_select_month()     # June select
        p5.click_select_year()      # 2026 select
        p5.click_select_date()      # 13 click — done
