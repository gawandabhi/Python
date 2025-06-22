def Singleton(cls):
    instance = {}
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper

@Singleton
class Logger:
    pass

log1 = Logger()
log2 = Logger()

print(log1 is log2)