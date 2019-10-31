# 发邮件的库
import smtplib
# 邮件脚本
from email.mime.text import MIMEText

# SMTP服务器
SMTPServer = "smtp.163.com"
# 发送者邮箱的密码
passwd = "wuyugang1234"
sender = "18255163610@163.com"
# 设置发送的内容
message = "dogpi is a good man"

# 转换成邮件文本
msg = MIMEText(message)
# 标题
msg["Subject"] = "来自dogpi的邮件"
# 发送者
msg["From"] = sender

# 创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer,25)
# 登录邮箱
mailServer.login(sender,passwd)
# 发送邮件
mailServer.sendmail(sender,["18255163610@163.com","a823435202@qq.com"],msg.as_string())
# 退出邮箱
mailServer.quit()