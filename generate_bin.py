# -*- coding: utf-8 -*-

WS_H = 60
WS_L = 29
LED_NUM = 600
DATA_LEN = 24
WS2812_RST_NUM = 50


WS2812_RGB_Buff = [0] * (LED_NUM*DATA_LEN+WS2812_RST_NUM)  # 适当调整大小

# 模拟 WS2812 设置函数
def WS2812_Set(num, color):
    indexx = num * (3 * 8)
    R = (color & 0xFF0000) >> 16
    G = (color & 0x00FF00) >> 8
    B = (color & 0x0000FF)

    for i in range(8):
        # 这里用假定的 WS_H 和 WS_L 来表示高低电平
        WS2812_RGB_Buff[indexx + i] = (G << i) & 0x80
        WS2812_RGB_Buff[indexx + i + 8] = (R << i) & 0x80
        WS2812_RGB_Buff[indexx + i + 16] = (B << i) & 0x80

circle_idx = [
    [8.4, 0, 15, 44.5, 78],
    [7.4, 103, 131.5, 158.5, 187.4],
    [6.4, 211.5, 235, 258.5, 283.4],
    [5.4, 302.4, 324.5, 345.5, 365.4],
    [4.4, 383.4, 400, 417, 435.4],
    [3.4, 448.4, 463, 477, 491],
    [2.4, 501.4, 512.5, 523, 532.4],
    [1.4, 540, 546.5, 553, 560],
    [0.4, 566, 568, 570, 573.6],
    [0, 575, 0, 0, 0]
]
led_block = [[0, 0] for _ in range(44)]  # 假设最大数组长度为 40

for i in range(len(circle_idx)):
    for j in range(1, len(circle_idx[i])):
        if circle_idx[i][j] == 0.0:
            continue
        led_block[i * 4 + j - 1][0] = circle_idx[i][j] - circle_idx[i][0]
        led_block[i * 4 + j - 1][1] = circle_idx[i][j] + circle_idx[i][0]

# 模拟通过 LED 数组控制
block_idx = 0
block_flag = 1
LED_NUM = 100  # 设定 LED 数量
color = 0xFF00FF  # 设置一个颜色值

for i in range(LED_NUM):
    if block_flag and led_block[block_idx][0] <= i <= led_block[block_idx][1]:
        WS2812_Set(i, color)
    else:
        WS2812_Set(i, 0x00)
    while block_flag and i > led_block[block_idx][1]:
        block_idx += 1
        if block_idx > len(led_block) // 4:
            block_flag = 0

# 导出 WS2812_RGB_Buff 到二进制文件
def export_ws2812_buff(file_name, buffer):
    with open(file_name, 'wb') as f:
        f.write(bytearray(buffer))
        # for value in buffer:
        #     # 拆分为两个字节，按照小端顺序存储
        #     f.write(struct.pack('<H', value))  # <H 表示小端顺序的 16 位无符号整数
    print(f"Data exported to {file_name}")

# 调用导出函数
export_ws2812_buff('WS2812_RGB_Buff.bin', WS2812_RGB_Buff)