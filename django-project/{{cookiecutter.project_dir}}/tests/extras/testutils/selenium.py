from seleniumbase import BaseCase


class SeleniumTC(BaseCase):
    live_server_url: str = ""

    def setUp(self, masterqa_mode=False):
        super().setUp()
        from testutils.factories import SuperUserFactory

        super().setUpClass()
        self.admin_user = SuperUserFactory()
        self.admin_user._password = "password"

    def tearDown(self):
        self.save_teardown_screenshot()
        super().tearDown()
        self.admin_user.delete()

    def base_method(self):
        pass

    def open(self, url: str):
        self.maximize_window()
        return super().open(f"{self.live_server_url}{url}")

    def select2_select(self, element_id: str, value: str):
        self.slow_click(f"span[aria-labelledby=select2-{element_id}-container]")
        self.wait_for_element_visible("input.select2-search__field")
        self.click(f"li.select2-results__option:contains('{value}')")
        self.wait_for_element_absent("input.select2-search__field")

    def login_as_user(self, user=None):
        if user is not None:
            self.admin_user = user
        self.open("/login/")
        self.type("input[name=username]", f"{self.admin_user.username}")
        self.type("input[name=password]", f"{self.admin_user._password}")
        self.submit('input[value="Login"]')
        self.wait_for_ready_state_complete()

    def login(self, url=None):
        self.open("/admin/")
        if self.get_current_url() == f"{self.live_server_url}/admin/login/?next=/admin/":
            self.type("input[name=username]", f"{self.admin_user.username}")
            self.type("input[name=password]", f"{self.admin_user._password}")
            self.submit('input[value="Log in"]')
            self.wait_for_ready_state_complete()

    def is_required(self, element: str) -> bool:
        el = self.wait_for_element_visible(element)
        return el.parent.find_element("label>span").text == "(required)"

    def get_field_error(self, element: str) -> bool:
        return self.wait_for_element_visible(f"fieldset.{element} ul.errorlist").text

    def get_pixel_colors(self):
        # Return the RGB colors of the canvas element's top left pixel
        x = 0
        y = 0
        if self.browser == "safari":
            x = 1
            y = 1
        color = self.execute_script(
            f"return document.querySelector('canvas').getContext('2d').getImageData({x},{y},1,1).data;"
        )
        if self.is_chromium():
            return [color[0], color[1], color[2]]
        return [color["0"], color["1"], color["2"]]


TestBrowser = SeleniumTC
