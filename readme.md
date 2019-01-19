# 调用API请求数据

## 补充包说明

### 使用huobi源

使用之前需要自行申请API token。注意保存token，不要泄露，如果只是查询数据的话不要开交易的权限。

使用Python需要补充的包，在命令行运行以下命令

```python
# 复制火币官方demo
git clone https://github.com/huobiapi/REST-Python3-demo
```

### 使用tushare源

参考源：https://tushare.pro/register?reg=231272

可以使用多种语言进行调用。上传的部分主要是Python的。全部的API接口名称、权限请参考tushare官网资料。

使用之前需要自行在网站上注册并获取token。

使用Python需要补充的包，在命令行运行以下命令：

```python
# 安装拓展包
pip install tushare
```

## 功能介绍

### bc_value

用来读取特定交易对在交易所的行情。由于数据库限制，最早的数据只能追溯到2017年10月11日，同时数据库不开放1min、5min频率的交易行情。

### bc_exchange

读取各个区域的交易所名称。

### cctv-news

获取每日新闻联播新闻播报内容。

### bc_value_huobi

使用火币交易所的API。

## 代理设置

使用huobi的API时，需要使用Proxifilter作为小飞机的二级代理。