from blueness import module
from bluer_options.help.functions import help_main

from blue_ai import NAME
from blue_ai.help.functions import help_functions

NAME = module.name(__file__, NAME)


help_main(NAME, help_functions)
