# network_dbg

## 说明 
scan vlan tool
这是一个交换机允许通过的vlan标签的脚本，查看服务器间允许通过的vlan标签

## 配置
修改python脚本中nic_name作为发包口

## 启动
1.在对端服务器启动tcpdump
2.在服务器启动python send.py
3.听到的vlan id表示交换机端允许通过的vlan标


