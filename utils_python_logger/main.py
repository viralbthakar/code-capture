import os
import argparse
from configs.get_logger import init_logger
from test_script import test_logger
from module_a.test_script_2 import test_logger_2
from module_b.test_script_3 import test_logger_3

logger = init_logger(os.path.splitext(os.path.basename(__file__))[0])


def main():
    print("Hello World!")
    print("Testing Logging from Main file ...")
    logger.info(f"Hello Information from {__file__}!")
    logger.error(f"Hello Error from {__file__}!")
    logger.warning(f"Hello Warning from {__file__}!")
    logger.debug(f"Hello Debug from {__file__}!")

    print("Testing Logging from File Next to Main Script ...")
    test_logger()

    print("Testing Logging from Module_a ...")
    test_logger_2()

    print("Testing Logging from Module_b ...")
    test_logger_3()


if __name__ == "__main__":
    main()
