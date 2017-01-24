#coding=utf-8   
import subprocess
child = subprocess.Popen(["ping","-c","5","www.google.com"])
print("parent process")

#child.poll() # 检查子进程状态
#child.kill() # 终止子进程
#child.send_signal() # 向子进程发送信号
#child.terminate() # 终止子进程
#子进程的PID存储在child.pid。