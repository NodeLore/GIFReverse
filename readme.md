# GIF分割反转器
> 斗图的时候突然发现的需求，虽然现在也有在线GIF编辑器，但只提供了编辑和排序功能，没法快捷实现反转

### Dependency
* Python 3.8
* Numpy 1.19.4
* Pillow 8.0.1
* imageio 2.9.0
* 在Windows10环境下开发，使用conda管理环境，运行时需要先运营activate激活conda，否则imageio在引入时可能报错

### Usage
> 拆解模式 默认情况下会直接拆解到当前路径的gif目录下，若不存在则创建，可以自行修改

`python split.py s [gifname]`

> 拼装模式 自动从当前路径下的gif目录下获取并反转拼接，生成指定名称的gif图片

`python split.py g [newname]`
