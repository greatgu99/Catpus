import io
import qrcode
import requests
from PIL import Image, ImageFont, ImageDraw, ImageOps
 
 
def gen_poster():
    """生成分享海报"""
    # 读取头像
    head_url = 'http://thirdwx.qlogo.cn/mmopen/fgHCN0LBhreDWUia2uicXHn0JS1FA86xNtkiafrIx71HV3fzkztqXTraqf3XB44hiaPESlhQqnalpUEX7DpCcFWXKlIQiaaeJUHbX/132'  # 头像
    head_res = requests.get(head_url)
    head_image = Image.open(io.BytesIO(head_res.content))
    head_image = head_image.resize((120, 120))  # 设定图片大小
 
    # 读取背景图
    back_image = 'https://static.interval.im/scrm/dPbnkRS5ttfxjMb7.jpeg'  # 背景
    back_res = requests.get(back_image)
    back_image = Image.open(io.BytesIO(back_res.content))
    back_image = back_image.resize((1080, 1920))  # 设定图片大小
 
    # 如果头像要求是圆形，做一个罩子把四角遮住
    size = (120, 120)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    head_cover = ImageOps.fit(head_image, mask.size, centering=(0.5, 0.5))
    head_cover.putalpha(mask)
    # 如果要求是方形，head_cover忽略
    back_image.paste(head_image, (48, 48), head_cover)  # 将头像贴在背景图上
 
    nickname = '风吹叶落^_^'  # 昵称
    location = (216, 84)  # 昵称位置
    font_color = '#FFFFFF'  # 设置字体颜色
    font_size = 12  # 字体大小
    font_path = './香港民间字集.otf'  # 本地读取的字体文件
    font = ImageFont.truetype(font_path, font_size * 3)
    obj = ImageDraw.Draw(back_image)
    obj.text(location, nickname, font_color, font=font)  # 将昵称贴在背景图上
 
    # 合成二维码
    code_url = ''  # 二维码跳转链接
    qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=8, border=0)
    qr.add_data(code_url)
    qr.make(fit=True)
    img = qr.make_image()
    qr_code = img.resize((270, 270))  # 设置二维码大小
    qr_location = (48, 1602)  # 二维码位置
    back_image.paste(qr_code, qr_location)  # 将二维码图片贴在背景图上
 
    # 展示成品图
    back_image.show()
    return 'success'
 
 
if __name__ == '__main__':
    gen_poster()