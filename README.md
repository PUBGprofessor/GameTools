# 造梦西游3 自动打造/强化

## 依赖库：

- pyautogui

- pytesseract

- PIL

（requirements.txt）

## 自动打造：

**utils.py -> build()**

## 自动强化：

**utils.py ->strengthen()**

*注：变量全在函数里面*

## Two tricks:

### 1.对图像预处理后，使用pytesseract库

使用简单的pytesseract OCR提取文本速度快，缺点是识别精度低，因此图像预处理：裁剪出文本所在位置的图像-->根据字体颜色提取字体所在像素，其余像素置为全黑-->输入进pytesseract提取出字符串-->转为int

即：



![tmpbncycand](C:\Users\刘佳豪\Pictures\Saved Pictures\tmpbncycand.PNG)

**-->**

![tmpsw6c1y9d](C:\Users\刘佳豪\Pictures\Saved Pictures\tmpsw6c1y9d.PNG)

**-->**

**237 = int("237")**

### 2.对于强化任务，只检测一个像素

强化任务只有“强化成功”“强化失败”两种情况，可只检测两种情况中某个像素不同的点，加快速度：

![屏幕截图 2025-01-06 004109](C:\Users\刘佳豪\Pictures\Screenshots\屏幕截图 2025-01-06 004109.png)

#### vs

![屏幕截图 2025-01-06 004118](C:\Users\刘佳豪\Pictures\Screenshots\屏幕截图 2025-01-06 004118.png)



## 参考文献：

【1】https://blog.csdn.net/dcrmg/article/details/102963336?fromshare=blogdetail&sharetype=blogdetail&sharerId=102963336&sharerefer=PC&sharesource=m0_74167177&sharefrom=from_link

【2】https://blog.csdn.net/qq_41567921/article/details/134813496?fromshare=blogdetail&sharetype=blogdetail&sharerId=134813496&sharerefer=PC&sharesource=m0_74167177&sharefrom=from_link

【3】Python OCR工具pytesseract详解 - 头还没秃的文章 - 知乎https://zhuanlan.zhihu.com/p/448253254