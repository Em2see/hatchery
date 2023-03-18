from loguru import logger
import sys
from . import cli


if __name__ == '__main__':
    logger.info('run')
    logger.info(sys.argv)
    cli(sys.argv[1:])
