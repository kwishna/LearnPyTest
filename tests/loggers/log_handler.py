import logging
import sys
import inspect

class LogHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.console_handler = logging.StreamHandler(sys.stdout)
        self.console_handler.setFormatter(logging.Formatter("%(asctime)s|%(levelname)s|%(module)s|%(message)s"))

    def emit(self, record):
        # Get the current frame and outer frames
        frame = inspect.currentframe()
        outer_frames = inspect.getouterframes(frame)

        # Create a new record with the outer frame information
        new_record = logging.makeLogRecord(record.__dict__)

        # Update the record with the outer frame information
        new_record.module = outer_frames[1].frame.f_globals['__name__']

        # Emit the new record
        self.console_handler.emit(new_record)