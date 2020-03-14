## env versions
* Python version:`3.6.4`
* PyCharm version:`2017.3.4.0`
* opencv-python version:`4.1.2.30`

## PyCharm + github
* commit error:`no tracked branch`
    * success: `git push --set-upstream origin master`
* commit success, but remote(github) not update
    * need commit + push

## PyCharm环境配置
#### PyCharm markdown支持粘贴图片
先安装官方推荐的Markdown support插件，再安装Paste images into MarkDown
#### PyCharm 执行代码报错，用命令行正常
```
new_code = types.CodeType(len(varnames),
TypeError: an integer is required (got type bytes)
```
解决： 是pycharm 与 python的版本不匹配，更新最新pycharm就行

## github 代码提交快捷键
* 提交到本地仓库  
    1. ctrl + k   
    2. 添加修改日志  
    3. 点击`commit`按钮即可  
* 提交到远程仓库  
    1. ctrl + k  
    2. 添加修改日志  
    3. ctrl + alt + k 
    4. 点击提交按钮即可    
