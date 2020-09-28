from   os import system
import time
import os


# DICT
PYTHON_DICT_OPEN          = " = {"
PYTHON_DICT_END           = "}"
CPSN_DICT_OPEN            = ": dict"
CPSN_DICT_END             = "</dict>"

# FUNCTIONS
PYTHON_FUNC_DECLARATION   = "def "
PYTHON_FUNC_OPEN          = ":"
PYTHON_FUNC_END           = ""
PYTHON_FUNC_CALL          = "()"
CPSN_FUNC_DECLARATION     = "func "
CPSN_FUNC_OPEN            = " {"
CPSN_FUNC_OPEN_2          = "{"
CPSN_FUNC_OPEN_3          = "\n{"
CPSN_FUNC_OPEN_4          = "\t{"
CPSN_FUNC_OPEN_5          = "\n:"
CPSN_FUNC_END             = "}"
CPSN_FUNC_CALL            = ".call"

# BOOLEANS
PYTHON_TRUE               = "True"
PYTHON_FALSE              = "False"
CPSN_TRUE                 = "true"
CPSN_FALSE                = "false"

# EOS
PYTHON_EOS                = ""
CPSN_EOS                  = ""

# IO
PYTHON_INPUT              = "= input()"
PYTHON_OUTPUT_OPEN        = "print("
PYTHON_OUTPUT_END         = ")"
CPSN_INPUT                = "<< input"
CPSN_OUTPUT_OPEN          = "<output>"
CPSN_OUTPUT_END           = "</output>"

# COMMENTS
PYTHON_COMMENT            = "#"
CPSN_COMMENT              = "//"

# IMPORT
PYTHON_IMPORT             = "import"
CPSN_IMPORT               = "#using "

# SCOPES
PYTHON_SCOPE_OPEN         = ""
PYTHON_SCOPE_END          = " "
CPSN_SCOPE_OPEN           = "<region>"
CPSN_SCOPE_END            = "</region>"

# CONDITIONS
PYTHON_NOT                = "not "
PYTHON_IS_NOT             = "is not"
CPSN_NOT                  = "!"
CPSN_IS_NOT               = "!="

# TYPES
PYTHON_GENERAL_ASSIGNMENT = " ="
PYTHON_INT                = ' = 0'
PYTHON_FLOAT              = ' = 0.0'
PYTHON_STRING             = ' = ""'
CPSN_INT                  = ": int"
CPSN_INT_2                = ": int ="
CPSN_FLOAT                = ": float"
CPSN_FLOAT_2              = ": float ="
CPSN_STRING               = ": string"
CPSN_STRING_2             = ": string ="

# CLASSES
PYTHON_CLASS              = "class "
PYTHON_CONSTRUCTOR        = "def __init__"
PYTHON_DECONSTRUCTOR      = "def __del__"
PYTHON_METHOD_OPEN        = ":"
PYTHON_METHOD_END         = ""
PYTHON_CLASS_END          = ""
PYTHON_NEW_CLASS          = " = "
PYTHON_SELF               = "self"
CPSN_CLASS                = "<class> "
CPSN_CONSTRUCTOR          = "<constructor>"
CPSN_DECONSTRUCTOR        = "<deconstructor>"
CPSN_METHOD_DECLARATION   = "<method> "
CPSN_METHOD_OPEN          = "<>"
CPSN_METHOD_END           = "</>"
CPSN_CLASS_END            = "</class>"
CPSN_NEW_CLASS            = ": new "
CPSN_SELF                 = "this"

# OPERATORS
PYTHON_IN                 = "in"
PYTHON_EQUALS             = "="
CPSN_IN                   = "->"
CPSN_EQUALS               = "<-"

# REPLACE
PYTHON_FORMAT_OPEN        = "{"
PYTHON_FORMAT_END         = "}"
CPSN_FORMAT_OPEN          = "<<"
CPSN_FORMAT_END           = ">>"





def build(source, mode="compile"):
    lines = []

    with open("temp.cpsn", "w") as temp:
        temp.write(source)

    with open("temp.cpsn", "r") as temp_read:
        lines = temp_read.readlines()

    for line in lines:
        if "#using " in line:
            linex      = line.strip("#using").strip("\n").strip(" ")
            _lines     = ""

            with open(f"{linex}.cpsn", "r") as line_file:
                _lines = line_file.read()

            source = source.replace(line, _lines + "\n")

    source = source.replace(CPSN_EQUALS,             PYTHON_EQUALS)

    source = source.replace(CPSN_FUNC_OPEN_4,        PYTHON_FUNC_OPEN)
    source = source.replace(CPSN_FUNC_OPEN_3,        PYTHON_FUNC_OPEN)
    source = source.replace(CPSN_FUNC_OPEN_5,        PYTHON_FUNC_OPEN)
    source = source.replace(CPSN_FUNC_DECLARATION,   PYTHON_FUNC_DECLARATION)
    source = source.replace(CPSN_FUNC_OPEN,          PYTHON_FUNC_OPEN)
    source = source.replace(CPSN_FUNC_END,           PYTHON_FUNC_END)
    source = source.replace(CPSN_FUNC_OPEN_2,        PYTHON_FUNC_OPEN)
    source = source.replace(CPSN_FUNC_CALL,          PYTHON_FUNC_CALL)

    with open("temp.CPSN", "w") as temp:
        temp.write(source)

    with open("temp.CPSN", "r") as temp_read:
        lines = temp_read.readlines()

    for line in lines:
        if "\t:" in line:
            linez  = "\n:\n"
            source = source.replace(line, linez)
            source = source.replace(CPSN_FUNC_OPEN_5, PYTHON_FUNC_OPEN)

    for line in lines:
        if "\t:" in line:
            linez  = "\n:\n"
            source = source.replace(line, linez)
            source = source.replace(CPSN_FUNC_OPEN_5, PYTHON_FUNC_OPEN)

    source = source.replace(CPSN_EQUALS,              PYTHON_EQUALS)

    source = source.replace(CPSN_FUNC_OPEN_4,         PYTHON_FUNC_OPEN)
    source = source.replace(CPSN_FUNC_OPEN_3,         PYTHON_FUNC_OPEN)
    source = source.replace(CPSN_FUNC_OPEN_5,         PYTHON_FUNC_OPEN)
    source = source.replace(CPSN_FUNC_DECLARATION,    PYTHON_FUNC_DECLARATION)
    source = source.replace(CPSN_FUNC_OPEN,           PYTHON_FUNC_OPEN)
    source = source.replace(CPSN_FUNC_END,            PYTHON_FUNC_END)
    source = source.replace(CPSN_FUNC_OPEN_2,         PYTHON_FUNC_OPEN)
    source = source.replace(CPSN_FUNC_CALL,           PYTHON_FUNC_CALL)

    source = source.replace(CPSN_INT_2,               PYTHON_GENERAL_ASSIGNMENT)
    source = source.replace(CPSN_FLOAT_2,             PYTHON_GENERAL_ASSIGNMENT)
    source = source.replace(CPSN_STRING_2,            PYTHON_GENERAL_ASSIGNMENT)

    source = source.replace(CPSN_INT,                 PYTHON_INT)
    source = source.replace(CPSN_FLOAT,               PYTHON_FLOAT)
    source = source.replace(CPSN_STRING,              PYTHON_STRING)

    source = source.replace(CPSN_IS_NOT,              PYTHON_IS_NOT)

    source = source.replace(CPSN_SCOPE_OPEN,          PYTHON_SCOPE_OPEN)
    source = source.replace(CPSN_SCOPE_END,           PYTHON_SCOPE_END)
    source = source.replace(CPSN_FORMAT_OPEN,         PYTHON_FORMAT_OPEN)
    source = source.replace(CPSN_FORMAT_END,          PYTHON_FORMAT_END)

    source = source.replace(CPSN_DICT_OPEN,           PYTHON_DICT_OPEN)
    source = source.replace(CPSN_DICT_END,            PYTHON_DICT_END)

    source = source.replace(CPSN_TRUE,                PYTHON_TRUE)
    source = source.replace(CPSN_FALSE,               PYTHON_FALSE)

    source = source.replace(CPSN_EOS,                 PYTHON_EOS)

    source = source.replace(CPSN_OUTPUT_OPEN,         PYTHON_OUTPUT_OPEN)
    source = source.replace(CPSN_OUTPUT_END,          PYTHON_OUTPUT_END)

    source = source.replace(CPSN_COMMENT,             PYTHON_COMMENT)

    source = source.replace(CPSN_CLASS,               PYTHON_CLASS)
    source = source.replace(CPSN_CONSTRUCTOR,         PYTHON_CONSTRUCTOR)
    source = source.replace(CPSN_DECONSTRUCTOR,       PYTHON_DECONSTRUCTOR)
    source = source.replace(CPSN_METHOD_OPEN,         PYTHON_METHOD_OPEN)
    source = source.replace(CPSN_METHOD_END,          PYTHON_METHOD_END)
    source = source.replace(CPSN_CLASS_END,           PYTHON_CLASS_END)
    source = source.replace(CPSN_METHOD_DECLARATION,  PYTHON_FUNC_DECLARATION)
    source = source.replace(CPSN_NEW_CLASS,           PYTHON_NEW_CLASS)
    source = source.replace(CPSN_SELF,                PYTHON_SELF)

    source = source.replace(CPSN_IN,                  PYTHON_IN)

    return source
