class Customer:

    name = None
    mail = None

    def __init__(self, mail, name):
        self.mail = mail
        self.name = name

    def get_formated_email(self):
        return "{} <{}>".format(self.name,self.mail)

    def get_total_price(self,value):
        return value
