import requests
from datetime import datetime

counter = 0
try:
  with open("counter.txt", "r") as f:
    counter = int(f.read())
except(FileNotFoundError):
  with open("counter.txt", "w") as f:
    f.write(str(counter))

counter = counter + 40

with open("counter.txt", "w") as f:
    f.write(str(counter))

def generate_svg(number):
    # Рассчитываем ширину прямоугольника фона на основе количества цифр
    num_digits = len(str(number))
    # Начальная ширина 80, увеличиваем на 20 за каждые 2 цифры после первой
    width = 80 + 20 * ((num_digits - 1) // 2)
    
    svg_content = f'''
<svg width="300" height="60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="a" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#320AB4"/>
      <stop offset="100%" stop-color="#B4A0FF"/>
    </linearGradient>
    <mask id="b">
      <rect width="100%" height="100%" fill="#fff"/>
      <rect x="40%" y="1" width="55" height="60" rx="30" ry="30"/>
    </mask>
  </defs>
  <rect x="0%" y="16%" width="50%" height="70%" rx="20" ry="20" fill="url(#a)" mask="url(#b)"/>
  <text x="20%" y="52%" fill="#fff" stroke="#000" stroke-width=".4" font-size="22" text-anchor="middle" dominant-baseline="middle">Km rolled</text>
  <rect id="number_bkg" x="41%" y="1" width="{width}" height="60" rx="30" ry="30" fill="#fff"/>
  <text x="54%" y="51%" fill="url(#a)" stroke="#000" stroke-width=".4" font-size="22" text-anchor="middle" dominant-baseline="middle">{number}</text>
</svg>
'''
    return svg_content

def save_svg(number, filename="output.svg"):
    svg = generate_svg(number)
    with open(filename, "w") as file:
        file.write(svg)
    print(f"SVG сохранен в файл {filename}")


save_svg(counter)
