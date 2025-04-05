from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')  # Setup code (like __enter__)
    try:
        yield f          # Yield control to the with block
    finally:
        f.close()        # Cleanup code (like __exit__)