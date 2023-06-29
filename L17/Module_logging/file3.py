import logging

logging.basicConfig(level=logging.INFO, filename="log_file3.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
x_vals = [2, 3, 6, 4, 10]
y_vals = [5, 7, 12, 0, 1]

for x_val, y_val in zip(x_vals, y_vals):
    x = x_val
    y = y_val
    logging.info(f"The values of x and y are {x} and {y}.")
    try:
        result = x / y
        logging.info(f"x/y successful with result: {result}.")
    except ZeroDivisionError as err:
        logging.exception("ZeroDivisionError")
