import sys
import os
import logging

# Configure logger
logger = logging.getLogger("DevOpsApp")


def setup_logging(debug_mode=False):
    """Set up log level and format based on debug flag."""
    level = logging.DEBUG if debug_mode else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    logger.setLevel(level)


def add(a, b):
    """Return the sum of two numbers."""
    logger.debug("Executing add(%s, %s)", a, b)
    result = a + b
    logger.debug("Result of add(%s, %s) = %s", a, b, result)
    return result


def subtract(a, b):
    """Return the difference of two numbers."""
    logger.debug("Executing subtract(%s, %s)", a, b)
    result = a - b
    logger.debug("Result of subtract(%s, %s) = %s", a, b, result)
    return result


def multiply(a, b):
    """Return the product of two numbers."""
    logger.debug("Executing multiply(%s, %s)", a, b)
    result = a * b
    logger.debug("Result of multiply(%s, %s) = %s", a, b, result)
    return result


def divide(a, b):
    """Return the quotient of two numbers."""
    logger.debug("Executing divide(%s, %s)", a, b)
    if b == 0:
        logger.error("Division by zero error: divide(%s, %s)", a, b)
        raise ValueError("Cannot divide by zero.")
    result = a / b
    logger.debug("Result of divide(%s, %s) = %s", a, b, result)
    return result


if __name__ == "__main__":
    is_debug = "--debug" in sys.argv or os.getenv("LOG_LEVEL") == "DEBUG"
    setup_logging(debug_mode=is_debug)

    logger.info("Starting DevOps Automation App (Debug Mode: %s)", is_debug)

    res_add = add(5, 10)
    print("Addition =", res_add)

    res_sub = subtract(10, 5)
    print("Subtraction =", res_sub)

    res_mul = multiply(5, 10)
    print("Multiplication =", res_mul)

    res_div = divide(10, 2)
    print("Division =", res_div)

    logger.info("Application execution finished successfully.")
