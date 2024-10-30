import os
import time
import yaml
import logging
import logging.config


def init_logger(name, log_dir="./logs"):
    # Set up logging
    log_dir = os.path.join(
        log_dir,
        os.path.basename(name),
        time.strftime("%Y-%m-%d"),
        time.strftime("%H-%M-%S"),
    )
    os.makedirs(log_dir, exist_ok=True)

    # Set up logging paths
    info_log_path = os.path.join(log_dir, "info.log")
    error_log_path = os.path.join(log_dir, "error.log")

    # Load the YAML config and apply it
    with open("./configs/logging_config.yaml", "r") as f:
        config = yaml.safe_load(f.read())
        config["handlers"]["info_file_handler"]["filename"] = os.path.join(
            log_dir, "info.log"
        )
        config["handlers"]["error_file_handler"]["filename"] = os.path.join(
            log_dir, "error.log"
        )
        logging.config.dictConfig(config)

    return logging.getLogger(name)
