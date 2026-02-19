def test_ExceptionErr(message):
    raise Exception(message)

def test_NameErr(message):
    raise NameError(message)

def test_KeyErr(message):
    raise KeyError(message)

def test_OSErr(message):
    raise OSError(message)

def test_ArithmeticErr(message):
    raise ArithmeticError(message)

def test_OverflowErr(message):
    raise OverflowError(message)

def test_ZeroDivisionErr(message):
    raise ZeroDivisionError(message)

def test_FloatingPointErr(message):
    raise FloatingPointError(message)

def test_AssertionErr(message):
    raise AssertionError(message)

def test_AttributeErr(message):
    raise AttributeError(message)

def test_BufferErr(message):
    raise BufferError(message)

def test_EOFErr(message):
    raise EOFError(message)

def test_ImportErr(message):
    raise ImportError(message)

def test_ModuleNotFoundErr(message):
    raise ModuleNotFoundError(message)

def test_LookupErr(message):
    raise LookupError(message)

def test_IndexErr(message):
    raise IndexError(message)

def test_MemoryErr(message):
    raise MemoryError(message)

def test_NotImplementedErr(message):
    raise NotImplementedError(message)

def test_BlockingIOErr(message):
    raise BlockingIOError(message)

def test_BrokenPipeErr(message):
    raise BrokenPipeError(message)

def test_ChildProcessErr(message):
    raise ChildProcessError(message)

def test_ConnectionErr(message):
    raise ConnectionError(message)

def test_ConnectionAbortedErr(message):
    raise ConnectionAbortedError(message)

def test_ConnectionRefusedErr(message):
    raise ConnectionRefusedError(message)

def test_ConnectionResetErr(message):
    raise ConnectionResetError(message)

def test_FileExistsErr(message):
    raise FileExistsError(message)

def test_FileNotFoundErr(message):
    raise FileNotFoundError(message)

def test_InterruptedErr(message):
    raise InterruptedError(message)

def test_IsADirectoryErr(message):
    raise IsADirectoryError(message)

def test_NotADirectoryErr(message):
    raise NotADirectoryError(message)

def test_PermissionErr(message):
    raise PermissionError(message)

def test_ProcessLookupErr(message):
    raise ProcessLookupError(message)

def test_TimeoutErr(message):
    raise TimeoutError(message)

def test_RecursionErr(message):
    raise RecursionError(message)

def test_StopIterationErr(message):
    raise StopIteration(message)

def test_StopAsyncIterationErr(message):
    raise StopAsyncIteration(message)

def test_SyntaxErr(message):
    raise SyntaxError(message)

def test_IndentationErr(message):
    raise IndentationError(message)

def test_TabErr(message):
    raise TabError(message)

def test_SystemErr(message):
    raise SystemError(message)

def test_TypeErr(message):
    raise TypeError(message)

def test_ValueErr(message):
    raise ValueError(message)

def test_WarningErr(message):
    raise Warning(message)

def test_GeneratorExitErr(message):
    raise GeneratorExit(message)

def test_KeyboardInterruptErr(message):
    raise KeyboardInterrupt(message)

def test_SystemExitErr(message):
    raise SystemExit(message)

def test_help():
    print("For futher information about error's - check the official documentation, and add to every error without Error, add Err in end, or if it has it, then just delete or in end of Error.")