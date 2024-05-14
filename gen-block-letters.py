from pathlib import Path
from string import Template
import unicodedata as ud

TEMPLATE = Template("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 36">
  <style>.main { font: bold 30px "Inter Alia"; fill: #fff; }</style>
  <path fill="$COLOR"
    d="M36 32c0 2.209-1.791 4-4 4H4c-2.209 0-4-1.791-4-4V4c0-2.209 1.791-4 4-4h28c2.209 0 4 1.791 4 4v28z" />
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" class="main">$LETTER</text>
</svg>""")


letters = list(map(chr, range(0x10450, 0x10480))) + ['·']
red_letters = '𐑚'

out = Path('out')
out.mkdir(exist_ok=True)

for letter in letters:
    name = ud.name(letter).split()[-1].lower()
    path = out.joinpath(f'regional_indicator_{name}.svg')

    content = TEMPLATE.substitute(COLOR='#3B88C3', LETTER=letter)
    path.write_text(content)

for letter in red_letters:
    name = ud.name(letter).split()[-1].lower()
    path = out.joinpath(f'{name}.svg')

    content = TEMPLATE.substitute(COLOR='#DD2E44', LETTER=letter)
    path.write_text(content)

