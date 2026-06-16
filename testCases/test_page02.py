import pytest
from Pages.Page02 import Page02

@pytest.mark.skip
@pytest.mark.usefixtures("setup")
class Test_Pagetwo:

    def test_verify(self):
        p2 = Page02(self.driver)
        p2.element_page()
        p2.upload_and_download()
        p2.download()
