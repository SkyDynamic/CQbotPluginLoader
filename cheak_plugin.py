import pkgutil

_plugins_before_listen = []  #插件列表
nameSet = set() 

def cheak_plugin():
    for finder,name,ispck in pkgutil.walk_packages(["./plugin"]):   #要主要这个文件目录参数是一个列表 
        loader = finder.find_module(name)  #返回一个loader对象或者None。
        mod = loader.load_module(name) #返回一个module对象或者raise an exception
        nameSet.add(mod.SLUG)  #用SLUG来标识每个功能模块
        _plugins_before_listen.append(mod) #把模块加入列表中，方便使用
    return _plugins_before_listen
