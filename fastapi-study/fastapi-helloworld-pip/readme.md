/root/miniconda3/bin/conda run --no-capture-output -n fastapi python /data/apps/fastapi-helloworld/main.py

```
vi /etc/systemd/system/fastapi-helloworld.service
```

```
[Unit]
Description=fastapi-helloworld
After=network.target

[Service]
Type=simple
User=root
Restart=on-failure
RestartSec=5s
WorkingDirectory = /data/apps/fastapi-helloworld
ExecStart=/root/miniconda3/bin/conda run --no-capture-output -n fastapi python /data/apps/fastapi-helloworld/main.py

[Install]
WantedBy=multi-user.target
```

systemctl start fastapi-helloworld
systemctl status fastapi-helloworld
systemctl stop fastapi-helloworld
systemctl enable fastapi-helloworld