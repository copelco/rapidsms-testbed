from routerq.backends import BackendBase


class WebformBackend(BackendBase):

    name = 'webform'

    def outgoing(self, msg):
        self.debug(msg)
