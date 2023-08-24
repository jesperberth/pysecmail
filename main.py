import extract_msg
import re

f = r'test1.msg'  # Replace with yours
msg = extract_msg.Message(f)
msg_body = msg.body

reg = re.compile('[0-9]+(?:\.[0-9]{1,3}){3}')

ip = re.findall( reg, msg_body )

print(ip)

