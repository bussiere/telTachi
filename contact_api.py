import atom
import gdata.data
import gdata.contacts.client
import gdata.contacts.data

def main():

  admin_email = ''
  admin_password = ''
  domain_index = admin_email.find('@')
  domain = admin_email[domain_index+1:]

  contacts_client = gdata.contacts.client.ContactsClient(domain=domain)
  contacts_client.client_login(email=admin_email,
                               password=admin_password,
                               source='shared_contacts_profiles',
                               account_type='HOSTED')

  new_contact = gdata.contacts.data.ContactEntry()
  new_contact.name = gdata.data.Name(
     full_name=gdata.data.FullName(text='John Doe'))
  new_contact.email.append(gdata.data.Email(address='john.doe@example.com',
     primary='true',rel=gdata.data.WORK_REL))
  feed_url = contacts_client.GetFeedUri(contact_list=domain, projection='full')
  contact_entry = contacts_client.CreateContact(new_contact, insert_uri=feed_url)

  print("Contact's ID: %s" % contact_entry.id.text)

if __name__ == '__main__':
  main()