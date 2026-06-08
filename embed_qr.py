# -*- coding: utf-8 -*-
import re

with open(r'C:\Users\21342\Desktop\sixian-edu\images\qr_compressed_b64.txt', 'r', encoding='utf-8') as f:
    b64 = f.read()

data_uri = f'data:image/jpeg;base64,{b64}'

files = [
    r'C:\Users\21342\Desktop\sixian-edu\引流-免费领资料.html',
    r'C:\Users\21342\Desktop\sixian-edu\引流-A4海报.html',
]

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace any existing data:image src with the new one
    html = re.sub(r'src="data:image/[^"]+"', f'src="{data_uri}"', html)

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)
    print('done:', fp.split('\\')[-1])
