我的MAC上有两个Python版本

系统自带：python2.7

自己安装：python3

为了可以尝试不同版本的开发，那么安装第三方库是就得多一层手续

Python2.7 路径：/System/Library/Python/2.7

Python3   路径：/usr/local/Frameworks/Python.framework/Versions/

### 安装beautifulsoup4

##### Python2.7安装

通过系统软件包来安装：$ apt-get install Python-bs4；

也可以通过easy_install或pip安装：$ easy_install beautifulsoup4，$ pip install beautifulsoup4。

##### Python3安装

下载bs4：http://www.crummy.com/software/BeautifulSoup/#Download

切只解压后的目录：python3 setup.py install