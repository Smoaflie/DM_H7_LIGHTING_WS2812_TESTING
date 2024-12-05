#include "WS2812.h"
#include "string.h"
//显存数组，长度为 灯的数量*24+复位周期
uint16_t WS2812_RGB_Buff[LED_NUM*DATA_LEN+WS2812_RST_NUM] = {0}; 
 
/**
 * 函数：WS2812单灯设置函数
 * 参数：num:灯的位置，R、G、B分别为三个颜色通道的亮度，最大值为255
 * 作用：单独设置每一个WS2812的颜色
***/
void WS2812_Set(uint16_t num,uint32_t color)
{
  uint32_t indexx=(num*(3*8));
  uint16_t R,G,B;
  R = (color & 0xFF0000) >> 16;
  G = (color & 0x00FF00) >> 8;
  B = (color & 0x0000FF) >> 0;
  for (uint8_t i = 0;i < 8;i++)
  {
	//填充数组
	WS2812_RGB_Buff[indexx+i]      = (G << i) & (0x80)?WS_H:WS_L;
	WS2812_RGB_Buff[indexx+i + 8]  = (R << i) & (0x80)?WS_H:WS_L;
	WS2812_RGB_Buff[indexx+i + 16] = (B << i) & (0x80)?WS_H:WS_L;
  }
}
 
//WS2812初始化函数
void WS2812_Init()
{
	//设置关闭所有灯
  memset(WS2812_RGB_Buff, 0, sizeof(WS2812_RGB_Buff));
}

void WS2812_Start()
{
  //作用：调用DMA将显存中的内容实时搬运至定时器的比较寄存器
  HAL_TIM_PWM_Start_DMA(&htim1,TIM_CHANNEL_1,(uint32_t *)WS2812_RGB_Buff,sizeof(WS2812_RGB_Buff)/sizeof(uint16_t)); 
}