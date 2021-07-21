#! python3
# Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re


# get the text of the clipboard
# text = 'email@email.com hellotest another@email.test.com another@email.com +44 7870597616 12345678910'
text = str(pyperclip.paste())

# Find all phone numbers and email addresses in the text
emails = re.compile(r'\w+@\w+.\w+')
phone_numbers = re.compile(r'\+\d{2}\s\d{10}')
e = emails.findall(text)
p = phone_numbers.findall(text)
print(e)
print(p)

# Paste them onto the clipboard
pyperclip.copy(f'Email: {", ".join(e)}; Phone: {", ".join(p)}')
