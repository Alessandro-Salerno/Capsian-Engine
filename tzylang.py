from   os import system
import time
import os

# DICT
PYTHON_DICT_OPEN          = " = {"
PYTHON_DICT_END           = "}"
KFEL_DICT_OPEN            = ": dict"
KFEL_DICT_END             = "</dict>"

# FUNCTIONS
PYTHON_FUNC_DECLARATION   = "def "
PYTHON_FUNC_OPEN          = ":"
PYTHON_FUNC_END           = ""
PYTHON_FUNC_CALL          = "()"
KFEL_FUNC_DECLARATION     = "func "
KFEL_FUNC_OPEN            = " {"
KFEL_FUNC_OPEN_2          = "{"
KFEL_FUNC_OPEN_3          = "\n{"
KFEL_FUNC_OPEN_4          = "\t{"
KFEL_FUNC_OPEN_5          = "\n:"
KFEL_FUNC_END             = "}"
KFEL_FUNC_CALL            = ".call"

# BOOLEANS
PYTHON_TRUE               = "True"
PYTHON_FALSE              = "False"
KFEL_TRUE                 = "true"
KFEL_FALSE                = "false"

# EOS
PYTHON_EOS                = ""
KFEL_EOS                  = ""

# IO
PYTHON_INPUT              = "= input()"
PYTHON_OUTPUT_OPEN        = "print("
PYTHON_OUTPUT_END         = ")"
KFEL_INPUT                = "<< input"
KFEL_OUTPUT_OPEN          = "<output>"
KFEL_OUTPUT_END           = "</output>"

# COMMENTS
PYTHON_COMMENT            = "#"
KFEL_COMMENT              = "//"

# IMPORT
PYTHON_IMPORT             = "import"
KFEL_IMPORT               = "#using "

# SCOPES
PYTHON_SCOPE_OPEN         = ""
PYTHON_SCOPE_END          = " "
KFEL_SCOPE_OPEN           = "<region>"
KFEL_SCOPE_END            = "</region>"

# CONDITIONS
PYTHON_NOT                = "not "
PYTHON_IS_NOT             = "is not"
KFEL_NOT                  = "!"
KFEL_IS_NOT               = "!="

# TYPES
PYTHON_GENERAL_ASSIGNMENT = " ="
PYTHON_INT                = ' = 0'
PYTHON_FLOAT              = ' = 0.0'
PYTHON_STRING             = ' = ""'
KFEL_INT                  = ": int"
KFEL_INT_2                = ": int ="
KFEL_FLOAT                = ": float"
KFEL_FLOAT_2              = ": float ="
KFEL_STRING               = ": string"
KFEL_STRING_2             = ": string ="

# CLASSES
PYTHON_CLASS              = "class "
PYTHON_CONSTRUCTOR        = "def __init__"
PYTHON_DECONSTRUCTOR      = "def __del__"
PYTHON_METHOD_OPEN        = ":"
PYTHON_METHOD_END         = ""
PYTHON_CLASS_END          = ""
PYTHON_NEW_CLASS          = " = "
PYTHON_SELF               = "self"
KFEL_CLASS                = "<class> "
KFEL_CONSTRUCTOR          = "<constructor>"
KFEL_DECONSTRUCTOR        = "<deconstructor>"
KFEL_METHOD_DECLARATION   = "<method> "
KFEL_METHOD_OPEN          = "<>"
KFEL_METHOD_END           = "</>"
KFEL_CLASS_END            = "</class>"
KFEL_NEW_CLASS            = ": new "
KFEL_SELF                 = "this"

# OPERATORS
PYTHON_IN                 = "in"
PYTHON_EQUALS             = "="
KFEL_IN                   = "->"
KFEL_EQUALS               = "<-"

# REPLACE
PYTHON_FORMAT_OPEN        = "{"
PYTHON_FORMAT_END         = "}"
KFEL_FORMAT_OPEN          = "<<"
KFEL_FORMAT_END           = ">>"





def build(source, mode="compile"):
    lines = []

    with open("temp.kfel", "w") as temp:
        temp.write(source)

    with open("temp.kfel", "r") as temp_read:
        lines = temp_read.readlines()

    for line in lines:
        if "#using " in line:
            linex      = line.strip("#using").strip("\n").strip(" ")
            _lines     = ""

            with open(f"{linex}.kfel", "r") as line_file:
                _lines = line_file.read()

            source = source.replace(line, _lines + "\n")

    source = source.replace(KFEL_EQUALS,             PYTHON_EQUALS)

    source = source.replace(KFEL_FUNC_OPEN_4,        PYTHON_FUNC_OPEN)
    source = source.replace(KFEL_FUNC_OPEN_3,        PYTHON_FUNC_OPEN)
    source = source.replace(KFEL_FUNC_OPEN_5,        PYTHON_FUNC_OPEN)
    source = source.replace(KFEL_FUNC_DECLARATION,   PYTHON_FUNC_DECLARATION)
    source = source.replace(KFEL_FUNC_OPEN,          PYTHON_FUNC_OPEN)
    source = source.replace(KFEL_FUNC_END,           PYTHON_FUNC_END)
    source = source.replace(KFEL_FUNC_OPEN_2,        PYTHON_FUNC_OPEN)
    source = source.replace(KFEL_FUNC_CALL,          PYTHON_FUNC_CALL)

    with open("temp.kfel", "w") as temp:
        temp.write(source)

    with open("temp.kfel", "r") as temp_read:
        lines = temp_read.readlines()

    for line in lines:
        if "\t:" in line:
            linez  = "\n:\n"
            source = source.replace(line, linez)
            source = source.replace(KFEL_FUNC_OPEN_5, PYTHON_FUNC_OPEN)

    for line in lines:
        if "\t:" in line:
            linez  = "\n:\n"
            source = source.replace(line, linez)
            source = source.replace(KFEL_FUNC_OPEN_5, PYTHON_FUNC_OPEN)

    source = source.replace(KFEL_EQUALS,              PYTHON_EQUALS)

    source = source.replace(KFEL_FUNC_OPEN_4,         PYTHON_FUNC_OPEN)
    source = source.replace(KFEL_FUNC_OPEN_3,         PYTHON_FUNC_OPEN)
    source = source.replace(KFEL_FUNC_OPEN_5,         PYTHON_FUNC_OPEN)
    source = source.replace(KFEL_FUNC_DECLARATION,    PYTHON_FUNC_DECLARATION)
    source = source.replace(KFEL_FUNC_OPEN,           PYTHON_FUNC_OPEN)
    source = source.replace(KFEL_FUNC_END,            PYTHON_FUNC_END)
    source = source.replace(KFEL_FUNC_OPEN_2,         PYTHON_FUNC_OPEN)
    source = source.replace(KFEL_FUNC_CALL,           PYTHON_FUNC_CALL)

    source = source.replace(KFEL_INT_2,               PYTHON_GENERAL_ASSIGNMENT)
    source = source.replace(KFEL_FLOAT_2,             PYTHON_GENERAL_ASSIGNMENT)
    source = source.replace(KFEL_STRING_2,            PYTHON_GENERAL_ASSIGNMENT)

    source = source.replace(KFEL_INT,                 PYTHON_INT)
    source = source.replace(KFEL_FLOAT,               PYTHON_FLOAT)
    source = source.replace(KFEL_STRING,              PYTHON_STRING)

    source = source.replace(KFEL_IS_NOT,              PYTHON_IS_NOT)

    source = source.replace(KFEL_SCOPE_OPEN,          PYTHON_SCOPE_OPEN)
    source = source.replace(KFEL_SCOPE_END,           PYTHON_SCOPE_END)
    source = source.replace(KFEL_FORMAT_OPEN,         PYTHON_FORMAT_OPEN)
    source = source.replace(KFEL_FORMAT_END,          PYTHON_FORMAT_END)

    source = source.replace(KFEL_DICT_OPEN,           PYTHON_DICT_OPEN)
    source = source.replace(KFEL_DICT_END,            PYTHON_DICT_END)

    source = source.replace(KFEL_TRUE,                PYTHON_TRUE)
    source = source.replace(KFEL_FALSE,               PYTHON_FALSE)

    source = source.replace(KFEL_EOS,                 PYTHON_EOS)

    source = source.replace(KFEL_OUTPUT_OPEN,         PYTHON_OUTPUT_OPEN)
    source = source.replace(KFEL_OUTPUT_END,          PYTHON_OUTPUT_END)

    source = source.replace(KFEL_COMMENT,             PYTHON_COMMENT)

    source = source.replace(KFEL_CLASS,               PYTHON_CLASS)
    source = source.replace(KFEL_CONSTRUCTOR,         PYTHON_CONSTRUCTOR)
    source = source.replace(KFEL_DECONSTRUCTOR,       PYTHON_DECONSTRUCTOR)
    source = source.replace(KFEL_METHOD_OPEN,         PYTHON_METHOD_OPEN)
    source = source.replace(KFEL_METHOD_END,          PYTHON_METHOD_END)
    source = source.replace(KFEL_CLASS_END,           PYTHON_CLASS_END)
    source = source.replace(KFEL_METHOD_DECLARATION,  PYTHON_FUNC_DECLARATION)
    source = source.replace(KFEL_NEW_CLASS,           PYTHON_NEW_CLASS)
    source = source.replace(KFEL_SELF,                PYTHON_SELF)

    source = source.replace(KFEL_IN,                  PYTHON_IN)

    return source
