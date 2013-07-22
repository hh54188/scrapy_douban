# 文件夹说明

flask内为网站的运行文件
其他的几个文件夹均为不同类库的尝试与制作的DEMO

#### 为什么不使用scrapy：

scrapy天生就是网络爬虫看。虽然强大，但依赖C++组件，并且很难把它抽象为类，实例化使用。
目前有一个[解决方案](http://www.tryolabs.com/Blog/2011/09/27/calling-scrapy-python-script/)，但这个方案要使用到多线程，介于这个工具部署在免费的Paas平台上，线程的使用时禁止的。所以抛弃scrapy

如何运行scrapy(二选一)
 - python run.py
 - scrapy crawler douban

幸运的是我要抓取的数据非常简单，关键在于解析HTML就够了，beautifulSoup4就可以满足

# requirement

- Flask==0.10.1
- beautifulsoup4==4.2.1
- pymongo==2.5.2 (可选)

推荐使用`virtualenv`来配置虚拟环境并且运行程序：

在本机安装好 `virtualenv` 后
1. 切换至工程文件夹 `$ cd project`
2. 创建虚拟环境 `$ virtualenv venv`
3. 使用虚拟环境(Windows) `$ venv\scripts\activate`
4. 退出虚拟环境 `$ deactivate`

注意：
- 在windows下务必使用自带cmd为命令行工具，不可使用git bash，否则无法进入虚拟环境
- repo克隆在不同pc上时务必重新运行 `$ virtualenv venv` 命令，重新部署环境

# 关于运行

运行 `python run.py` 即可
注意，`run.py` 是把数据存储在一个变量（内存）中。但基于flask框架不稳定，推荐运行`run_mongo.py` 版本。将数据存储在mongoDB中（你需要在本地安装mongoDB和在python
中安装pymongo）

### 参数设置

`run.py`:
- `EXPIRE_TIME`：更新时间间隔，以秒为单位

`info.py`:
- `FETCH_URLS`: 要抓取的豆瓣小组链接
- `PAGE_NUM`: 每个小组要抓取的页数
- `PAUSE_SECOND`: 每一条链接抓取之间的时间间隔
