import json

with open("zap-report.json") as f:
    data = json.load(f)

warn = 0
fail = 0
info = 0

for site in data["site"]:
    for alert in site["alerts"]:
        risk = alert["riskdesc"].lower()

        if "high" in risk:
            fail += 1
        elif "medium" in risk:
            warn += 1
        elif "low" in risk:
            info += 1

score = 100 - (fail*40 + warn*10 + info*2)

if score < 0:
    score = 0

print(f"Security Score: {score}/100")

with open("reports/security-score.md","w") as f:
    f.write(f"# Security Score\n\n")
    f.write(f"Score: **{score}/100**\n\n")
    f.write(f"- High: {fail}\n")
    f.write(f"- Medium: {warn}\n")
    f.write(f"- Low: {info}\n")