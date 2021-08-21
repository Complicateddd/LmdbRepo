# LmdbRepo
简单快速LMDB框架、写入pytorch dataloader后训练读数据会快很多倍

### 1、多线程处理大量小文件（10w+）：

例如：

- 对每个mp4切音频、
- 对每个视频用VGG提取特征并保存
- 核心代码复写

```python
python Multi_thread_session.py
```

### 2、多线程LMDB数据储存：

复写核心代码块

针对train、val、test生成key-val形式

文件夹 Train-0、Train-1 ...

```python
python LMDB_multi_thread_session.py
```

### 3、LMDB_Dataloder：

​		LMDB_dataloder.py
