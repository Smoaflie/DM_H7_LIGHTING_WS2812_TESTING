#include "main.h"
#include "tim.h"
 
#define WS_H           60   // 1 码相对计数值
#define WS_L           29   // 0 码相对计数值
#define WS_REST        40   // 复位信号脉冲数量
#define LED_NUM        600   // WS2812灯个数
#define DATA_LEN       24   // WS2812数据长度，单个需要24个字节
#define WS2812_RST_NUM 50   // 官方复位时间为50us（40个周期），保险起见使用50个周期
 
void WS2812_Init(void);
void WS2812_Set(uint16_t num,uint32_t color);
void WS2812_Start();