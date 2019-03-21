class PoolEmptyError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return repr("进程池中没有进程")
