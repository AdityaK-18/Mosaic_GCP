# central logging setup for entire project
# without centrslized logging, every dev setup logging differently
# print() or logging.basicConfig()

# every log - uniform
# timestamp | log level | while file it came from | message

from email import message
import logging # log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
import sys # we are going to write all the logs to stdout
# so cloud run captures them auto
# cloud run reads the stdout & sends it to google cloud logging

def setup_logging(name:str)-> logging.logger:
    '''
    This function is called at the top of every py file
    each file will get its own logger, namedspaced to that file path
    this means log lines will show, which file generated then
    '''
    logger = logging.getLogger(name)
    #getLogger(name) either creates a new logger or returns an existing one
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    # set minimum log level to INFO
    handler = logging.StreamHandler(sys.stdout)
    # stream handler sends log lines to the stream
    #formatter

    # asctime IN THIS format - %Y-%m-%d %H:%M:%S
    # levelname -8s - Log level (DEBUG, INFO, ERROR, WARNING
    # %(name)s -> Name of the logger
    # %(message)s - The actual log message
    formatter = logging.Formatter("%(asctime)s | %(levelname)-8s'|%(name)s | %{message}",
                                  datefmt="%Y-%m-%d %H:%M:%S",

    )
    handler.setFormatter(formatter)
    # attach the formatter to handler
    # handler now knows how to format each line before printing

    logger.addHandler(handler)
    # attach handler to the logger
    # now when you call logger.info("something"), it flows:
    # logger -> handler -> formatter -> stdout -> terminal
    logger.propagate = False
    # cuts the record off at that logger. 
    # Its own handlers run, and the bubbling stops.
    return logger
