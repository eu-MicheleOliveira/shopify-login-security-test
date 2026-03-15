import requests

url="https://sauce-demo.myshopify.com/account/login"

payloads=open("fuzzing/payloads.txt").read().splitlines()

results=[]

for payload in payloads:

    data={
        "customer[email]":payload,
        "customer[password]":payload
    }

    r=requests.post(url,data=data)

    results.append((payload,r.status_code))

with open("reports/fuzzing-results.md","w") as f:

    f.write("# Fuzzing Results\n\n")

    for payload,status in results:

        f.write(f"| Payload | Status |\n")
        f.write(f"|---|---|\n")
        f.write(f"| {payload} | {status} |\n")