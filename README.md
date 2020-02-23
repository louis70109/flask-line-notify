# Flask-LINE-notify

最近看到保哥寫了一篇 [LINE Notify 的文章](https://blog.miniasp.com/post/2020/02/17/Go-Through-LINE-Notify-Without-Any-Code)，詳細的介紹整個操作流程，這個專案則是去實作整個流程的範例。

# LINE Notify 註冊

可以參考我之前[鐵人賽的文章](https://nijialin.com/2019/09/20/Day5-%E5%81%9A%E4%B8%80%E5%80%8B%E8%88%87-LINE-Notify-%E9%80%A3%E5%8B%95%E7%9A%84%E6%9C%8D%E5%8B%99/)。

# 技能

- Python 3.7
- Flask
- LINE Notify

# 啟動

```sh
python api.py
```

或是

```dockerfile
docker-compose up
```

> 兩個方法擇一

# 使用

開啟瀏覽器後輸入 `http://localhost:5000/notify`後就會看到一個輸入按鈕

![](https://i.imgur.com/RraASZL.png)
點選之後會到 LINE 的綁定畫面，選`1對1聊天接收`
![](https://i.imgur.com/jhB3pMV.png)
這時候 LINE Notify 就會推播一個綁定成功的通知
![](https://i.imgur.com/0KlKrXE.png)
同時瀏覽器會被導到`/notify/check` 並帶上 code & state 的資訊
![](https://i.imgur.com/oGs5NWI.png)
接著再輸入框上輸入文字就會推播囉！
![](https://i.imgur.com/U9zZnmm.png)
結果出爐:
![](https://i.imgur.com/KjGXOo3.png)

# 路由

- GET /notify
  - 使用者點選綁定的畫面
- GET /notify/check
  - LINE Notify 認證完後的 callback 路由
- POST /notify/send
  - 幫忙發送推播的路由(因為有[ CORS 問題](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/CORS)所以需要一個 api 來幫忙轉發)

# License

The project is available as open source under the terms of the MIT License.
