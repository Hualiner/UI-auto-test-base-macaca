class LoginStatus:
    @classmethod
    def set_status(cls, status):
        cls.status = status

    def get_status(self):
        return self.status
