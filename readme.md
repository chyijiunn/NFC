# NFC
1. 本活動基於 PN532 與raspberry pi 連結後在 [pn532lib](https://github.com/HubCityLabs/py532lib) 套件協助下完成
1. 讀取 NTag215 內部資料後，獲取標籤 ID
1. 針對 ID 進行 MD5 雜湊，使用 [hashlib.md5]
1. 揭出控制硬體，如 sg90 馬達

# 課程內容
1. 16位元
1. NTag215資料格式
	* 資料格式
	* 手機讀取、寫入
1. 硬體接線
	* [I2C](https://pinout.xyz) > [圖示](/pics/GPIO.png)
	* 按鈕 I0 = 1 , I1 = 0 > [圖示](/pics/I0I1.jpg)
	* GND , VCC , SDA , SCL = pin 6 , 4 , 3 , 5 > [圖示](/pics/pn532.jpg)
1. 讀取 ID
## 雜湊演算：像果汁機一樣打到碎
特徵
	- 輸出長度相同
	- key -> value，相同 key 、相同 value
	- 類似的 key，差異很大的 value
	- hash collision 雜湊碰撞，機率低但會發生，不同 key 卻得到相同 value
	- value 無法換算回 key，不可逆
類別：不同演算方式、使用相同 key 得到不同 value
	-  MD5 (Message Digest Algorithm)
	-  SHA-1 (Secure Hash Algorithm)  [資安疑慮](https://zh.m.wikipedia.org/zh-tw/SHA家族)
	-  SHA-2 , SHA3-256 , 512
1. 寫入資料
# 流程圖
![](/pics/workflow.png)