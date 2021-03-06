# -*- coding: utf-8 -*-

import sys

from mynt.core import Mynt
from mynt.exceptions import MyntException


def main():
    try:
        Mynt()
    except MyntException as e:
        print(e)

        return e.code

    return 0


if __name__ == '__main__':
    sys.exit(main())
