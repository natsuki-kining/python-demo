# 四 网络编程

## 4.1 UDP
### 4.1.1 IP地址类别
<table>
    <tr>
        <th>IP地址类型</th>
        <th colspan="8">第一段</th>
        <th colspan="8">第二段</th>
        <th colspan="8">第三段</th>
        <th colspan="8">第四段</th>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td colspan="7">网络号7位</td>
        <td colspan="24">主机号24位</td>
    </tr>
    <tr>
        <td>A类</td>
        <td>0</td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td bgcolor=#D1EEEE></td>
        <td ></td>
        <td ></td>
        <td ></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td colspan="14">网络号14位</td>
        <td colspan="16">主机号24位</td>
    </tr>
    <tr>
        <td>B类</td>
        <td>1</td>
        <td>0</td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td colspan="21">网络号21位</td>
        <td colspan="8">主机号8位</td>
    </tr>
    <tr>
        <td>C类</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td colspan="28"></td>
    </tr>
    <tr>
        <td>D类</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td colspan="27"></td>
    </tr>
    <tr>
        <td>E类</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
        <td ></td>
    </tr>
</table>  

#### 4.1.1.1 A类IP地址
* 一个A类IP地址由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”，
* 地址范围1.0.0.1-126.255.255.254
* 二进制表示为：00000001 00000000 00000000 00000001 - 01111110 11111111 11111111 11111110
* 可用的A类网络有126个，每个网络能容纳1677214个主机

#### 4.1.1.2 B类IP地址
* 一个B类IP地址由2个字节的网络地址和2个字节的主机地址组成，网络地址的最高位必须是“10”，
* 地址范围128.1.0.1-191.255.255.254
* 二进制表示为：10000000 00000001 00000000 00000001 - 10111111 11111111 11111111 11111110
* 可用的B类网络有16384个，每个网络能容纳65534主机

#### 4.1.1.3 C类IP地址
* 一个C类IP地址由3字节的网络地址和1字节的主机地址组成，网络地址的最高位必须是“110”
* 范围192.0.1.1-223.255.255.254
* 二进制表示为: 11000000 00000000 00000001 00000001 - 11011111 11111111 11111110 11111110
* C类网络可达2097152个，每个网络能容纳254个主机

#### 4.1.1.4 D类地址用于多点广播
* D类IP地址第一个字节以“1110”开始，它是一个专门保留的地址。
* 它并不指向特定的网络，目前这一类地址被用在多点广播（Multicast）中
* 多点广播地址用来一次寻址一组计算机 s 地址范围224.0.0.1-239.255.255.254

#### 4.1.1.5 E类IP地址
* 以“1111”开始，为将来使用保留
* E类地址保留，仅作实验和开发用

#### 4.1.1.6 私有ip
* 在这么多网络IP中，国际规定有一部分IP地址是用于我们的局域网使用，也就是属于私网IP，不在公网中使用的，它们的范围是：
    * 10.0.0.0～10.255.255.255
    * 172.16.0.0～172.31.255.255
    * 192.168.0.0～192.168.255.255
    
#### 4.1.1.7 注意
* IP地址127．0．0．1~127．255．255．255用于回路测试，
    * 如：127.0.0.1可以代表本机IP地址，用http://127.0.0.1就可以测试本机中配置的Web服务器。

### 4.1.2 端口
> 在linux系统中，端口有65536（2的16次方）个之多

#### 4.1.2.1 端口是怎样分配的
端口的分类标准有好几种，下面只介绍一下知名端口和动态端口

##### 4.1.2.1.1 知名端口（Well Known Ports）
知名端口是众所周知的端口号，范围从0到1023
> 80端口分配给HTTP服务  
> 443端口分配给HTTPS服务  
> 21端口分配给FTP服务

##### 4.1.2.1.2 动态端口（Dynamic Ports）
* 动态端口的范围是从1024到65535
* 之所以称为动态端口，是因为它一般不固定分配某种服务，而是动态分配。
* 动态分配是指当一个系统程序或应用程序程序需要网络通信时，它向主机申请一个端口，主机从可用的端口号中分配一个供它使用。
* 当这个程序关闭时，同时也就释放了所占用的端口号

##### 4.1.2.1.3 怎样查看端口
* linux上
    * 用“netstat －an”查看端口状态
    * lsof -i [tcp/udp]:2425
    
* windows上
    * netstat -aon | findstr "8080" 获取PID
    
    
### 4.1.3 socket
#### 4.1.3.1 创建socket
在 Python 中 使用socket 模块的函数 socket 就可以完成：
```python
import socket
socket.socket(AddressFamily, Type)
```
* Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET
* Type：套接字类型，可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议）或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）



#### 4.1.3.2 创建一个tcp socket（tcp套接字）

#### 4.1.3.3 创建tcp的套接字
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ...这里是使用套接字的功能（省略）...

# 不用的时候，关闭套接字
s.close()
```


#### 4.1.3.4 创建udp的套接字
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ...这里是使用套接字的功能（省略）...

# 不用的时候，关闭套接字
s.close()
```

### 4.1.4 udp网络程序-发送、接收数据

#### 4.1.4.1 udp网络程序-发送、接收数据
创建一个基于udp的网络程序流程很简单，具体步骤如下：
1. 创建客户端套接字
2. 发送/接收数据
3. 关闭套接字

```python
#coding=utf-8

from socket import *

# 1. 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 准备接收方的地址
dest_addr = ('192.168.236.129', 8080)

# 3. 从键盘获取数据
send_data = input("请输入要发送的数据:")

# 4. 发送数据到指定的电脑上
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

# 5. 等待接收对方发送的数据
recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数

# 6. 显示对方发送的数据
# 接收到的数据recv_data是一个元组
# 第1个元素是对方发送的数据
# 第2个元素是对方的ip和端口
print(recv_data[0].decode('gbk'))
print(recv_data[1])

# 7. 关闭套接字
udp_socket.close()
```

### 4.1.5 python3编码转换
```python
value = value.decode(encoding="utf-8", errors="strict")
value = value.encode(encoding="utf-8", errors="strict")
```





