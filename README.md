# 环境安装使用说明

- linux
1. 安装antlr
    ```sh
    $ mv files/antlr-4.13.0-complete.jar /usr/local/lib
    $ cd /usr/local/lib
    $ export CLASSPATH=".:/usr/local/lib/antlr-4.13.0-complete.jar:$CLASSPATH"
    $ alias antlr4='java -jar /usr/local/lib/antlr-4.13.0-complete.jar'
    $ alias grun='java org.antlr.v4.gui.TestRig'

    ## 在bashrc文件中添加以下三行内容
    export CLASSPATH=".:/usr/local/lib/antlr-4.13.0-complete.jar:$CLASSPATH"

    alias antlr4='java -jar /usr/local/lib/antlr-4.13.0-complete.jar'
    alias grun='java org.antlr.v4.gui.TestRig'

    ```
2. 如开发环境为Python，使用`pip3 install antlr4-python3-runtime`
3. 确认相关软件及依赖安装完成后，下载已有的语法文件`git clone git@github.com:antlr/grammars-v4.git`
4. 根据语法文件生成相关解析器。执行命令`antlr -Dlanguage=Python3 grammars-v4/sql/postgresql/PostgreSQLLexer.g4`，`antlr -Dlanguage=Python3 grammars-v4/sql/postgresql/PostgreSQLParser.g4`生成解析器，解析器在语法文件目录下
- MacOs
1. 安装antlr`brew install antlr`
2. 如开发环境为Python，使用`pip3 install antlr4-python3-runtime`
3. 确认相关软件及依赖安装完成后，下载已有的语法文件`git clone git@github.com:antlr/grammars-v4.git`
4. 根据语法文件生成相关解析器。执行命令`antlr -Dlanguage=Python3 grammars-v4/sql/postgresql/PostgreSQLLexer.g4`，`antlr4 -Dlanguage=Python3 grammars-v4/sql/postgresql/PostgreSQLParser.g4`生成解析器，解析器在语法文件目录下

# 使用说明
1. 引入依赖和解析器
```py
from antlr import *
import 
```
2. 