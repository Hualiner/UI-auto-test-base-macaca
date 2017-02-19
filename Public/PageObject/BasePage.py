class BasePage(object):
    @classmethod
    def set_driver(cls, dri):
        cls.driver = dri

    def get_driver(self):
        return self.driver
