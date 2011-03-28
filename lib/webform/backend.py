from routerq.backends import BackendBase


class WebformBackend(BackendBase):

    def send(self, msg):
        self.debug(msg)
