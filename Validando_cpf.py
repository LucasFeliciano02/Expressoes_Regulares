# FEITO NO SITE REGEX101
# https://regex101.com/r/XPy0Qc/1

"""
VALIDANDO CPF COM NEGATIVE LOOKAHEAD
"""

import re
from pprint import pprint


# (?!  = POR SER NEGATIVE LOOKAHEAD PARA N DAR MATCH EM SEQUENCIAS
regex = re.compile(
    r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$",
    flags=re.MULTILINE
)

test_str = ("698.547.520-54\n"
            "060.235.190-16\n"
            "683.134.960-96\n"
            "899.344.730-62\n"
            "103.778.870-21\n"
            "721.478.580-30\n"
            "366.310.090-14\n"
            "794.289.350-26\n"
            "190.259.410-01\n"
            "000.000.000-01\n"
            "900.000.000-00\n\n"
            "000.000.000-00\n"
            "111.111.111-11\n"
            "222.222.222-22\n"
            "333.333.333-33\n"
            "444.444.444-44\n"
            "555.555.555-55\n"
            "666.666.666-66\n"
            "777.777.777-77\n"
            "888.888.888-88\n"
            "999.999.999-99\n\n"
            )

pprint(regex.findall(test_str))
