# Unittests and Integration Tests

**Unit tests** are used to test that when given ideal conditions, a specific unit/part of code works while **integration tests** are used to test that 2 or more parts of a program work well together as expected.

## Mocking

*Mocking* is used to abstract functions, classes, methods, or attributes to guarantee behavior when running tests.

### Mock vs MagicMock

```Mock()``` is the base class for mock objects while ```MagicMock()``` inherits from Mock() while adding 'magic methods' such as `__len__()` and `__str__()`.\
`MagicMock()` is more often used.

## MagicMock() parameters

`unittest.mock.MagicMock(spec=None, side_effect=None, return_value=DEFAULT, ...)`

+ **spec** *aka specifications*: list of strings or object/class specifications that the mocked object will take on.\
Can be used so that a mock_obj can pass a check using `isinstance()` when spec is set to a class or instance

+ **side_effect**: function, exception class/instance, or iterable

    1. When it is a **function**, this function is called when the mock object is called.\
    Can be a `lambda` function, whose parameters shall be those fed into the call of the mock object
    2. When it is an **exception class/instance**, this exception SHALL always be raised when the mock object is called.
    3. When it is an **iterable**, calling the mock object will return the next item in the iterable.\
    *Note*: the attr `side_effect` can be reset by setting it to `None`.

+ **return_value**: value to be returned when the mock object is called. Default behavior is returning another mock object.

## MagicMock() methods

+ **assert_called()**: raises if mock object has not been called
+ **assert_called_with(*args, \**kwargs)**: raises if the *last* call of the mock object was not made with specific parameters.
+ **assert_any_call(*args, \**kwargs)**: raises if the mock object has never been called with specific parameters.
+ **configure_mock(\**kwargs)**: sets the key-value pairs in kwargs as the attributes of the mock object.

## Patching

Patching allows to temporarily replace (patch) a target attribute or method with a mock object during a test.\
Can be used a decorator or as a context manager

`unittest.mock.patch(target, new_callable=None, create=False, ...)`

+ **target**: string in the form of 'package.module.target'. This is the target function, class, method or attribute to be patched.
+ **new_callable**: specifies the class from which the mock object will be created.\Default if `AsyncMock` for asynchronous objects and `MagicMock` for the rest.

## PropertyMock()

creates a mock object that is intended to be used a property of a class. This exposes `__get__()` and `__set__()` methods on the mock object.
