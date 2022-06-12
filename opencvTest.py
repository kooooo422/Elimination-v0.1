#coding:utf-8
import cv2
cap = cv2.VideoCapture(0)#建立一個 VideoCapture 物件

flag = 1 #設定一個標誌，用來輸出視訊資訊
num = 1 #遞增，用來儲存檔名
while(cap.isOpened()):#迴圈讀取每一幀
    ret_flag, Vshow = cap.read() #返回兩個引數，第一個是bool是否正常開啟，第二個是照片陣列，如果只設定一個則變成一個tumple包含bool和圖片
    cv2.imshow("Capture_Test",Vshow)  #視窗顯示，顯示名為 Capture_Test
    k = cv2.waitKey(1) & 0xFF #每幀資料延時 1ms，延時不能為 0，否則讀取的結果會是靜態幀
    if k == ord('s'):  #若檢測到按鍵 ‘s’，列印字串
        cv2.imwrite(str(num) + ".jpg", Vshow)
        print(cap.get(3)) #得到長寬
        print(cap.get(4))
        print("success to save"+str(num)+".jpg")
        print("-------------------------")
        num += 1
    elif k == ord('q'): #若檢測到按鍵 ‘q’，退出
        break
cap.release() #釋放攝像頭
cv2.destroyAllWindows()#刪除建立的全部視窗