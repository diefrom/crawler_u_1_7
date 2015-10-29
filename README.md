# crawler_u_1_7
===
声明：
1. 本程序仅仅是为了研究学习用，请勿用于私下盈利用途。
2. 如果用本程序下载漫画后，想要进行传播和复制等，请联系漫画原作者，尊重作家版权，谢谢！

## 使用示例
### 下载所有章节
```
[root@test python]# python crawler2015.py 
please input Web's URL: http://www.u17.com/comic/14325.html
select 1 to download the whole directory.
select 2 to download the part of chapter.
select 3 to download the image.
please input your selection: 1
```

### 下载部分章节
PS：在漫画网站上的目录页面从0计数，如以下例子将会下载《第三章.01》
```
[root@test crawler_u_1_7]# python crawler2015.py 
please input Web's URL: http://www.u17.com/comic/14325.html
select 1 to download the whole directory.
select 2 to download the part of chapter.
select 3 to download the image.
please input your selection: 2
please input the start of chapter: 10
please input the end of charpter: 11
```

### 附加程序：moveToOne.sh
使用crawler2015.py下载后会每一章节一个文件夹，如果想要把不同文件夹中的图片都移动到同一个文件夹中，可以将该文件移动到包含不同文件夹的文件下（如u17），运行即可。

