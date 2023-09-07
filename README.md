# pysecmail

reads msg files from fortigate with failed SSL-VPN logins

```bash

mkdir done messages output

docker build . -t pysecmail:latest

docker run -it --mount type=bind,source="$(pwd)"/done,target=/usr/src/app/done --mount type=bind,source="$(pwd)"/messages,target=/usr/src/app/messages --mount type=bind,source="$(pwd)"/output,target=/usr/src/app/output pysecmail:latest

```
