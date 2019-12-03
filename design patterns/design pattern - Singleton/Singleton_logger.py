# def write_log(filename, level, msg):
# with open(filename, "a") as log_file:
# log_file.write("[{0}] {1}\n".format(level, msg))
# def critical(msg):
# write_log("CRITICAL",msg)
# def error(msg):
# write_log("ERROR", msg)
# def warn(msg):
# write_log("WARN", msg)
# def info(msg):
# write_log("INFO", msg)
# def debug(msg):
# write_log("DEBUG", msg)

class logger:
    def __init__(self, fname):
        self._file_name = fname

    def _write_log(self, msg, log_level='Info'):
        with open(self._file_name, "a") as log_file:
            log_file.write("[{0}] {1}\n".format(log_level, msg))

    def critical(self, msg):
        self._write_log(msg, 'CRITICAL')

    def error(self, msg):
        self._write_log(msg, 'ERROR')

    def info(self, msg):
        self._write_log(msg, 'INFO')

    def debug(self, msg):
        self._write_log(msg, 'DEBUG')

