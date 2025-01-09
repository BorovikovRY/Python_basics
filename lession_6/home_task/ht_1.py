users = []
users.append("Kevin")
users.append("Bob")
users.append( "Alice")
print(users)
users.remove("Bob")
print(users)
rev_users = users[::-1]
print(rev_users)
users.insert(1,"Melody")
print(users)
users.extend(['Andy', 'Wanda', 'jim'])
print(users)
center_users = users[2:4]
print(center_users)