certificate_verify_flask
=========

## これは何？

SSL証明書の整合性をチェックするWEBツールです。  

## 使い方

### 0.必要なパッケージの導入

```
yum install python3 python3-devel
pip3 install flask flask-httpauth
```

### 1.レポジトリのclone

```
git clone [URL]
cd certificate_verify_flask
```

### 2.サーバの起動

```
./main.py
```

### 3.接続

ブラウザから接続する。

http://ipアドレス:5000/