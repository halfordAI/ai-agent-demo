class Singleton:
    _instance = None
    _is_initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not self._is_initialized:
            self.projectCode = value
            self._is_initialized = True

    def set_code(self, value):
        self.projectCode = value

    def get_code(self):
        return self.projectCode