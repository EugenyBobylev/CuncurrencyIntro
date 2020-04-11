from functools import wraps


def log_it(logfile='log.txt'):
    """
      Декоратор для журналирования обращения к функции
    :param f: функция
    """
    def logging_decorator(f):
        @wraps(f)
        def with_logging(*args, **kwargs):
            log_msg1 = f.__name__ + ' начали исполнять'
            _result = f(*args, **kwargs)
            log_msg2 = f.__name__ + ' была исполнена\n'
            with open(logfile, 'a') as log:
                log.write(log_msg1 + '\n')
                log.write(log_msg2 + '\n')
            return _result
        return with_logging
    return logging_decorator


@log_it(logfile='mylog.txt')
def add_something(x):
    return x + x


@log_it(logfile='logging.txt')
def print_something(msg):
    print(msg)
    return None


if __name__ == "__main__":
    result = add_something(1267)
    print_something(result)
