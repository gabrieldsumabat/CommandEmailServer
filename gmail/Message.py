class Message:
    def __init__(self, name, address, subject, content):
        self.name = name
        self.address = address
        self.subject = subject
        self.content = content

    def __str__(self):
        return "Name: \n%s \nAddress: \n%s \nSubject: \n%s\n\nContent: \n%s \n" % (
        self.name, self.address, self.subject, self.content)
