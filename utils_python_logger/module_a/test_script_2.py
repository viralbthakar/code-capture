import logging

logger = logging.getLogger(__name__)


def test_logger_2():
    logger.info("Hello Information from test_script_2.py!")
    logger.error("Hello Error from test_script_2.py!")
    logger.warning("Hello Warning from test_script_2.py!")
    logger.debug("Hello Debug from test_script_2.py!")
    assert True
