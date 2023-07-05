from  antlr4 import *
import sys,re
# sys.path.append("./grammars-v4/sql/plsql")
from PlSqlLexer import PlSqlLexer as lexer
from PlSqlParser import PlSqlParser as parser







def get_table(i_sql):
    lexerName = grammar + 'Lexer'
    parserName = grammar + 'Parser'
    module_lexer = __import__(lexerName, globals(),['./grammars-v4/sql/plsql'], lexerName)
    class_lexer = getattr(module_lexer, lexerName)
    module_parser = __import__(parserName, globals(), locals(), parserName)
    class_parser = getattr(module_parser, parserName)
    #input_stream = FileStream(file_name)
    input_stream = InputStream(i_sql.upper())
    lexer = class_lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = class_parser(token_stream)
    parser.buildParseTrees = True
    func_start_rule = getattr(parser, 'sql_script')
    parser_ret = func_start_rule()
    print('test')
    return parser_ret

def get_table_position( node):
    if isinstance(node, ParserRuleContext):
        class_name = str(type(node))
        if str(class_name)=="<class 'PlSqlParser.PlSqlParser.Tableview_nameContext'>":
            tb_list.append([re.split(r'[,:]',str(node.start))[1],re.split(r'[:=]',str(node.stop))[1]])
    if hasattr(node, 'children'):
        for child in getattr(node, 'children'):
            get_table_position(child)

# def main(sql):
#     input_stream = sql
#     lexers = lexer(input_stream)
#     stream = CommonTokenStream(lexers)
#     parser_sql = parser(stream)
#     tree = parser_sql.startRule()
#     return tree

#file_name=r'test.sql'
tb_list=[]
grammar='PlSql'
# start_rule='sql_script'

sql = "select abc from def,ghi j,k.lmn o"

get_table_position(get_table(sql))
print(tb_list)

# main(sql)

