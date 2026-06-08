"""Replace inline SVGs in math.html with MATLAB-generated SVGs."""
import re

html_path = r'C:\Users\21342\Desktop\sixian-edu\资料\数学.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# SVG filenames mapped in order of appearance
svg_files = [
    'model_01_handshake.svg',
    'model_02_k_shape.svg',
    'model_03_three_perp.svg',
    'model_04_median_double.svg',
    'model_05_angle_bisector.svg',
    'model_06_a_similar.svg',
    'model_07_8_similar.svg',
    'model_08_projection.svg',
    'model_09_half_angle.svg',
    'model_10_jiangjun.svg',
    'model_11_huguigui.svg',
    'model_12_apollonius.svg',
    'model_13_fermat.svg',
    'model_14_hidden_circle.svg',
    'model_15_guadou.svg',
    'model_16_fold.svg',
]

# Find all <svg ...> ... </svg> blocks inside geometric model section
# Match from <svg to </svg> (non-greedy, but handle nested tags)
count = 0
def replace_svg(match):
    global count
    if count >= len(svg_files):
        return match.group(0)
    fname = svg_files[count]
    count += 1
    return f'<img src="../gen_svg_out/{fname}" width="240" height="150" style="display:block;margin:0 auto" alt="">'

# Replace SVGs that have width="240"
new_html = re.sub(r'<svg\s+width="240"[^>]*>.*?</svg>', replace_svg, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f'Replaced {count} inline SVGs with <img> tags in math.html')
