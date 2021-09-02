# -*- encoding: utf-8 -*-

from soc_common.tools.code_generate.golang import generate_by_java
from soc_common.tools.toolkit.config import convert_unit


def main():
  convert_unit.build_config()


if __name__ == '__main__':
  generate_by_java.run()
