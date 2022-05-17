# ImageProcessing 影像處理平台開發 V3.0

   ![partybird](https://github.com/Night2155/ImageProcessing/blob/HOMEWORK_V2/image/PartyBird.gif)
+ 程式語言 Python
+ 套件 PyQt5、OpenCV
+ 開發工具 PyCharm、QtDesigner
+ 程式參考
   + [12th 鐵人賽 – 【錢不夠買ps的我，只好用OpenCV來修圖了!】](https://www.wongwonggoods.com/category/portfolio/12th_ironman/)
   + [仿射轉換](https://blog.csdn.net/liuweiyuxiang/article/details/82799999)
   + [透視投影轉換](https://blog.csdn.net/guduruyu/article/details/72518340)

基本功能 : 

1. 選單
    ```
    載入影像 
    儲存影像
    關閉平台
    ```
2. 色彩選項 (轉換色彩通道)
    ```
    灰階影像
    轉換原始影像
    灰階影像均衡化
    二值化影像
    HSV影像
    ```
3. 小工具
    ```
    選取ROI
    仿射轉換
    透視投影轉換
    顯示影像直方圖
    ```
4. 影像處理
    ```
    影像模糊化
    影像邊緣擷取
    影像雜訊處理
    ```
程式介面 :

 ![interface](https://github.com/Night2155/ImageProcessing/blob/HOMEWORK_V3/image/interface_v3.png)

# 程式檔案說明
   +  [Call_MainWindow.py](https://github.com/Night2155/ImageProcessing/blob/HOMEWORK_V3/Call_MainWindow_V3.py)
      + 程式啟動
      + 介面物件呼叫函式
   +  [ImageProcess.py](https://github.com/Night2155/ImageProcessing/blob/HOMEWORK_V3/ImageProcess.py)
      + 影像處裡函式
   +  [MainWindow.py](https://github.com/Night2155/ImageProcessing/blob/HOMEWORK_V3/MainWindow_V3.py)
      + 主程式介面設計

# 程式優化與BUG說明

BUG說明
```
(1.) 程式主畫面縮放時，內部物件無法跟著縮放
(2.) 影像變換色彩後，使用仿設轉換功能圖片無法轉換色彩
```
預計優化
```
(1.) 主程式介面縮放優化
(2.) 仿射轉換功能改善
(3.) 邊緣偵測閥值輸入方式改善 [QLineEdit]->[QSlider]
```
