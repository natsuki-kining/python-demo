# 利用Python进行数据分析 第二版
# 书名原文：Python for Data Analysis:Data Wrangling with Pandas,NumPy,and IPython,2nd Edition
# 代码示例：http://github.com/wesm/pydata-book
# 本书陈列勘误、示例和其他信息的地址：http://bit.ly/python_data_analysis_2e
# 官网：http://www.oreilly.com
# 作者个人网站：http://wesmckinney.com

# 一、第一章

### 1.4.4 安装及更新python包
* 安装anaconda并不包含的额外python包：
    * conda install package_name
    
* 如何不奏效可以使用pip包管理工具进行安装：
    * pip install package_name
    
* 还可以使用conda update命令来更新包：
    * conda update package_name
    
* pip还支持通过--upgrade 标识升级：
    * pip install -- upgrade package_name
    
    
# 二、Python语言基础、IPython及Jupyter notebook

### 2.2.4 内省
在Jupyter notebook中：  
在一个变量名的前后使用问号（？）可以显示一些关于该对象的概要信息 
使用？显示文档字符串  
使用？？显示函数的源代码  
？ 有一个终极用途，可以像标准Unix或windows命令行一样搜索IPython命名空间。  
把一些字符串和通配符（*）结合在一起，会显示所有匹配通配符表达式的命名。  
例：np.*load*?  
np.\_loader\_  
np.load  
np.loads