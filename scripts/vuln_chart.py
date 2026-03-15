import json
import matplotlib.pyplot as plt

with open("zap-report.json") as f:
    data = json.load(f)

high=0
medium=0
low=0

for site in data["site"]:
    for alert in site["alerts"]:
        risk = alert["riskdesc"].lower()

        if "high" in risk:
            high+=1
        elif "medium" in risk:
            medium+=1
        elif "low" in risk:
            low+=1

labels=["High","Medium","Low"]
values=[high,medium,low]

plt.bar(labels,values)

plt.title("Vulnerability Distribution")
plt.ylabel("Findings")

plt.savefig("reports/vulnerability-chart.png")