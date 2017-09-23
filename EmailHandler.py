
from myconfig import emailAdress, gmailPassword
import urllib2,urllib

_emailAdress, _gmailPassword = emailAdress, gmailPassword

class GmailHandler(object):
    def __init__(self, emailAdress, password):
        self.emailAdress = emailAdress
        self.password = password

    def logInToGmail(self):
        pass

    def tesT(self):
        url ="http://gmail.com"

        values = {'email': _emailAdress,
                  'password': _gmailPassword}
        data = urllib.urlencode(values)
        request = urllib2.Request(url, data)  # lub urllib2.Request(url, data=data)
        response = urllib2.urlopen(request)
        html = response.read()
        print html





PatrykGmail = GmailHandler(_emailAdress,_gmailPassword)
PatrykGmail.tesT()

