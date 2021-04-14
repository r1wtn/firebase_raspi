# systemd に登録する方法

## 実行プログラムの用意

- `get_gps.py` をホームディレクトリ 以下に配置.  
- `python3` で実行するため、ソースコードのはじめに以下を記載.

```py
#!/usr/bin/env python3
```

- 実行権限を与える.

```bash
chmod 0755 /home/<user_name>/get_gps.py
```

## サービスの作成

- 実行ユーザを指定することに注意.
- `get_gps.service` を作成

```bash
sudo vi /etc/systemd/system/get_gps.service
```


```service
[Unit]
Description=get gps daemon

[Service]
ExecStart=/home/<user_name>/get_gps.py
Restart=always
Type=simple
User=<user_name>

[Install]
WantedBy = multi-user.target
```

## サービスの登録

```bash
sudo systemctl enable get_gps.service
```

## アクティベート

```bash
sudo systemctl start get_gps.service
```

## 実行状態の確認・再起動

- ソースコードに誤りがあり、意図した挙動をしていない場合、以下のコマンドで確認する.

```bash
sudo systemctl status get_gps.service
```

- ソースコードを修正した場合、以下でサービスを再起動して反映する.


```bash
sudo systemctl restart get_gps.service
```