# -*- coding: utf-8 -*-
"""将两个引流页面的二维码替换为 base64 内嵌"""
import sys

# 读取 base64
sys.path.insert(0, r'C:\Users\21342\Desktop\sixian-edu\images')
from qr_data import QR_BASE64

DATA_URI = f'data:image/png;base64,{QR_BASE64}'

files = [
    r'C:\Users\21342\Desktop\sixian-edu\引流-免费领资料.html',
    r'C:\Users\21342\Desktop\sixian-edu\引流-A4海报.html',
]

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace the img tag. Both files use the same pattern:
    old_tag = 'src="images/qr-wechat.png"'
    new_tag = f'src="{DATA_URI}"'

    if old_tag in html:
        html = html.replace(old_tag, new_tag)
        # Also remove onerror hide since it would hide the error but not help
        html = html.replace(' onerror="this.style.display=\'none\'"', '')
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✅ {fp.split(chr(92))[-1]} 已更新')
    else:
        print(f'❌ {fp.split(chr(92))[-1]} 未找到替换目标')
