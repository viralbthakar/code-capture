import logging

logger = logging.getLogger(__name__)


def test_logger():
    logger.info("Hello Information from test_script.py!")
    logger.error("Hello Error from test_script.py!")
    logger.warning("Hello Warning from test_script.py!")
    logger.debug("Hello Debug from test_script.py!")
    assert True
