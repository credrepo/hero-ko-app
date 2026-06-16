def test_verity_all_test(self, setup):
    p5 = Page05(setup)

    p5.click_widget_btn()
    p5.click_date_picker()
    p5.select_picker()
    p5.click_select_month()
    p5.click_select_year()
    p5.click_select_time()    # ✅ PEHLE
    p5.click_select_date()    # ✅ BAAD MEIN
