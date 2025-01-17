# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from

def my_func():
    logging.debug("This is a debug-level log message", extra=extdata)

# set the output file and debug level, and
# TODO: use a custom formatting specification
fmtstr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d %(message)s"
datestr = "%m/%d/%Y %I:%M:%S %p"
extdata = {
    "user": "user@example.com"
}

logging.basicConfig(filename="output.log",
                    level=logging.DEBUG,
                    format=fmtstr,
                    datefmt=datestr)

logging.info("This is an info-level log message", extra=extdata)
logging.warning("This is a warning-level message", extra=extdata)
my_func()

