import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def timeit(func):
    """
    A decorator that measures and prints the execution time of a function.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(
            f"Function '{func.__name__}' executed in {execution_time:.4f} seconds."
        )
        return result

    return wrapper


# Apply the timing decorator
@timeit
def compute_square_sum(n):
    """
    A function that computes the sum of squares up to n.
    """
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    compute_square_sum(1000000)
