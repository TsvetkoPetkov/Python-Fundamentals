class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    command = input()

    if command == "Stop":
        break

    info_about_the_email = command.split()
    sender = info_about_the_email[0]
    receiver = info_about_the_email[1]
    content = info_about_the_email[2]

    curr_email = Email(sender, receiver, content)

    emails.append(curr_email)


indexes_to_send = [int(x) for x in input().split(", ")]

for inx, email in enumerate(emails):
    if inx in indexes_to_send:
        emails[inx].send()

for email in emails:
    print(email.get_info())
