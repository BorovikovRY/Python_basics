print("-" * 20)
import pprint
emails = {}
emails['ashley']= 'ashley@example.com'
emails['craig']= 'craig@example.com'
emails['elizabeth']= 'elizabeth@example.com'
pprint.pprint(emails)
print("-" * 20)
del emails ['craig']
pprint.pprint(emails)
print("-" * 20)
emails['dalton'] = 'dalton@example.com'
pprint.pprint(emails)
print("-" * 20)
users = list(emails.keys())
pprint.pprint(users)
email_list = list(emails.values())
pprint.pprint( email_list)
print("-" * 20)
pairs = list(emails.items())
pprint.pprint(pairs)
print("-" * 20)