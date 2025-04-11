import requests
from datetime import datetime

counter = 0
with open("counter.txt", "rw") as a:
  counter = int(a.read())
  counter++
  a.write(counter)

date = datetime.now().strftime("%d.%m.%Y")

svg = f'''
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="50">
  <rect width="100%" height="100%" fill="#5865F2" rx="4"/>
  <text x="10" y="20" fill="white" font-family="Arial" font-size="14">
    KM: {counter} | Updated: {date}
  </text>
</svg>
'''



with open("badge.svg", "w") as f:
  f.write(svg)
