# Kazoo

kazoo是Python连接操作ZooKeeper的客户端库。我们可以通过kazoo来使用ZooKeeper。

## 1. 安装

```shell
pip install kazoo
```

## 2. 使用

#### 连接ZooKeeper

```python
from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')

# 启动连接
zk.start() 

# 停止连接
zk.stop()  
```

#### 创建节点

```python
# 创建节点路径，但不能设置节点数据值
zk.ensure_path("/my/favorite")

# 创建节点，并设置节点保存数据，ephemeral表示是否是临时节点，sequence表示是否是顺序节点
zk.create("/my/favorite/node", b"a value", ephemeral=True, sequence=True)
```

#### 读取节点

```python
# 获取子节点列表
children = zk.get_children("/my/favorite")

# 获取节点数据data 和节点状态stat
data, stat = zk.get("/my/favorite")
```

#### 设置监视

```python
def my_func(event):
    # 检查最新的节点数据

# 当子节点发生变化的时候，调用my_func
children = zk.get_children("/my/favorite/node", watch=my_func)
```

