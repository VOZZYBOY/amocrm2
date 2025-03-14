import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Время выполнения: {end - start} сек")
    return wrapper

@timer
def test():
    time.sleep(2)

if __name__ == "__main__":
    test() 