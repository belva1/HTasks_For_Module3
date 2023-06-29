import logging

logging.basicConfig(level=logging.INFO, filename="log_file2.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

x = 3
y = 0

logging.info(f"The values of x and y are {x} and {y}.")
try:
    result = x / y
    logging.info(f"x/y successful with result: {result}.")
except ZeroDivisionError as err:
    logging.error("ZeroDivisionError", exc_info=True)
