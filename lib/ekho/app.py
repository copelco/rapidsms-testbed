from rapidsms.apps.base import AppBase


class EkhoApp(AppBase):
    
    def handle(self, msg):
        msg.respond('ekho {0}'.format(msg.text))
        return True
