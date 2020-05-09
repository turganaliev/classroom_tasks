class ContactList(list):
    def __init__(self, name):
        list.__init__(self)
        self.name = name

    def search_by_name(self):
        all_contacts = ['andrew', 'billie', 'lovelace', 'leon', 'billie']
        names = []
        for contact in all_contacts:
            if contact == self.name:
                names.append(self.name)
        print(names)

all_contacts = ContactList('billie')
all_contacts.search_by_name()
