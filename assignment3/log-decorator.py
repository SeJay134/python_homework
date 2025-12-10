# Task 1
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        positional = list(args) if args else "none"
        keywords = dict(kwargs) if kwargs else "none"
        result = func(*args, **kwargs)

        logger.log(
            logging.INFO,
            f"function: {func_name}\n"
            f"positional parameters: {positional}\n"
            f"keyword parameters: {keywords}\n"
            f"return: {result}\n"
            "----"
        )

        return result
    return wrapper

@logger_decorator
def hello_world():
    print("Hello World")

@logger_decorator
def many_positional(*args):
    return True

@logger_decorator
def many_keywords(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    hello_world()
    many_positional(1, 2, 3, "test", True)
    many_keywords(a=1, b=2, user="Alex")

    print("Done. Check decorator.log.")