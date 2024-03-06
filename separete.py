# Read the emails.txt file and rearrange emails with new domains
with open('emails.txt', 'r') as file:
    emails = file.read().split()

# Rearrange emails with new domains
domains = set()
rearranged_emails = []

for email in emails:
    domain = email.split('@')[-1]
    if domain not in domains:
        rearranged_emails.append(email)
        domains.add(domain)

for email in emails:
    domain = email.split('@')[-1]
    if domain in domains and email not in rearranged_emails:
        rearranged_emails.append(email)

# Write rearranged emails to newemails.txt file
with open('newemails.txt', 'w') as file:
    for email in rearranged_emails:
        file.write(email + '\n')
