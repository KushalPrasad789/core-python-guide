# Implement a logging class that allows only one instance.

class SingletonLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonLogger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.log_file = "logfile.log"
            with open(self.log_file, 'w') as file:
                file.write("Logger initialized\n")

    def log(self, message):
        with open(self.log_file, 'a') as file:
            file.write(message + "\n")

# Example usage:
logger1 = SingletonLogger()
logger2 = SingletonLogger()

logger1.log("This is the first log message.")
logger2.log("This is the second log message.")

print(logger1 is logger2)  # Output: True