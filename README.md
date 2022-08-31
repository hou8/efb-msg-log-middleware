# EFB Message Log Middleware

## 功能

将所有的消息按照月份记录在默认 storage 目录下，比如：
`~/.ehforwarderbot/profiles/default/hou8.msg_log/202208_log.json`

## 安装

```bash
pip install git+https://github.com/hou8/efb-msg-log-middleware
```

在 `config.yaml` 中配置本中间件：

```yaml
middlewares:
- other.othermiddleware
- hou8.msg_log
```
