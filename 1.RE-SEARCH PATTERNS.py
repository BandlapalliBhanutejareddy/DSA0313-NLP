import re
text=" teja33@gmail.com or 7893564252"
email_pattern = r"\w+@\w+.\w+"
phone_pattern = r"\d{10}"
email=re.search(email_pattern, text)
phone=re.search(phone_pattern, text)
if email:
    print("found email ", email.group())
else:
    print("not found")
if phone:
    print("found phone", phone.group())
else:
    print("not found")

