# ini_editor
Lightweight scripting to add/modify/delete/query specific format ini file

## Getting Started

Start by using `python3.7 ini_editor -h` to get all usage.

```shell
usage: ini_editor.py [-h] {doctor,query,add,modify,delete} ...

positional arguments:
  {doctor,query,add,modify,delete}
    doctor              检查依赖环境
    query               查询 SECTION 某个 KEY 的值
    add                 添加 KEY - VALUE 键值对到 SECTION 下
    modify              修改 SECTION 下某个 KEY 的值
    delete              删除 SECTION 下某个 KEY

optional arguments:
  -h, --help            show this help message and exit
```

**query operation：**

```shell
python3.7 ini_editor.py query [-h] -s SECTION -k KEY
```

**add operation：**

```shell
python3.7 ini_editor.py add [-h] -s SECTION -k KEY -v VALUE
```

**modify operation：**

```shell
python3.7 ini_editor.py modify [-h] -s SECTION -k KEY -v VALUE
```

**delete operation：**

```shell
python3.7 ini_editor.py delete [-h] -s SECTION -k KEY
```

### Deploying

Here Provide **setup.py**， so you can use setuptools to install it like this .

```
python3.7 setup.py sdist

pip3.7 install dist/ini_editor-1.0.0.tar.gz

# now you can use resign-brush anywhere
ini_editor -h
```

## Contributing