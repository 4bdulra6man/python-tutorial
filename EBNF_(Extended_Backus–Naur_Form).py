# https://docs.python.org/3/reference/compound_stmts.html#while

"""
while_stmt ::= "while" assignment_expression ":" suite
               ["else" ":" suite]
"""

# This is written in EBNF (Extended Backus–Naur Form), a formal way of describing a programming
# language's grammer.
# Breaking it down:

# `while-stmt` -> means the "a while statement"
# `::=` -> "is defined as"
# `while` -> literally the keyword "while"
# `assignment_expression` -> what comes right_after `while` (normally your condition)
# `:` -> literally the colon character
# `suite` -> means "one or more indented statements" (the body of the while loop)
# `["else" ":" suite]` -> the square brackets mean "this part is optional"

"""
import_stmt     ::= "import" module ["as" identifier] ("," module ["as" identifier])*
                    | "from" relative_module "import" identifier ["as" identifier]
                    ("," identifier ["as" identifier])*
                    | "from" relative_module "import" "(" identifier ["as" identifier]
                    ("," identifier ["as" identifier])* [","] ")"
                    | "from" relative_module "import" "*"
module          ::= (identifier ".")* identifier
relative_module ::= "."* module | "."+
"""

# import_stmt ::= ...

# This defines what counts as an import statement in Python.
# It has four possible forms (separated by | — which means “OR”).


# Supporting Rules: module and relative_module

# module ::= (identifier ".")* identifier
# Means a module can have dots in it — e.g., package.subpackage.module.

# relative_module ::= "."* module | "."+
# Means a relative import can be:

# zero or more dots + a module name (..subpackage.module)

# OR just dots (.. meaning “go up two levels and import init.py there”)

"""
from . import helpers     # from current package
from ..subpkg import mod  # go one level up then into subpkg.mod
from ... import utils     # go two levels up and import utils
"""