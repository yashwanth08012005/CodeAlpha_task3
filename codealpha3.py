import re
input_file = "input.txt"
output_file = "emails.txt"
with open(input_file, "r") as file:
    content = file.read()
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, content)
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("✅ Email extraction completed!")
print(f"📧 {len(emails)} email(s) saved to {output_file}")
