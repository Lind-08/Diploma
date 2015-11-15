import inspect
__author__ = 'lind'
__version__ = '1.0b'


def _empty_func():
        pass


class Event:
    def __init__(self, handler_sample=_empty_func):
        self.__handlers = list()
        self.__handler_sample = inspect.getargspec(handler_sample)

    def __del__(self):
        self.__handlers = None

    def __equal_handler(self, handler):
        if inspect.getargspec(handler).args == self.__handler_sample.args and\
                        inspect.getargspec(handler).varargs == self.__handler_sample.varargs:
            return True
        else:
            return False

    def __handle(self, handler):
        if self.__equal_handler(handler):
            self.__handlers.append(handler)
        else:
            raise ValueError("Handler args is not equal with event's args.")
        return self

    def __unhandle(self, handler):
        try:
            self.__handlers.remove(handler)
        except:
            raise ValueError("Handler is not handling this event, so cannot unhandle it.")
        return self

    def __raise(self, *args, **kargs):
        for handler in self.__handlers:
            handler(*args, **kargs)

    def clear(self):
        self.__handlers == list()

    __iadd__ = __handle

    __isub__ = __unhandle

    __call__ = __raise

if __name__ == "__main__":
    def test_hello_world():
        print("Hello, world!")

    def another_test_hello_world():
        print("Another Hello, world!")

    def wrong_test_hello_world(text):
        print(text)

    def func_with_parametres(a, b):
        print("{0} + {1} = {2}".format(a, b, a + b))

    print("Events module v{0}".format(__version__))

    print("Creation Event with empty signature and adding handler".center(68, '-'))
    test_event = Event(test_hello_world)
    test_event += test_hello_world
    test_event += another_test_hello_world
    test_event()

    print("Removing handler".center(68, '-'))
    test_event -= another_test_hello_world
    test_event()

    print("Adding handler with wrong signature".center(68, '-'))
    try:
        test_event += wrong_test_hello_world
    except ValueError:
        print("Error when you try to add handler with wrong signature.")
    test_event()

    print("Creation Event with empty signature and adding handler".center(68, '-'))
    test_event = Event(func_with_parametres)
    test_event += func_with_parametres
    test_event(1, 2)




