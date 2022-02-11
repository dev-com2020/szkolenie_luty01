import inspect
import asyncio
import time


async def f():
    yield 123


# print(type(f))
# gen = f()
#
# print(inspect.iscoroutinefunction(f))
# print(type(gen))
# coro = f()
# print(type(coro))


def count():
    print("Jeden")
    # await asyncio.sleep(1)
    time.sleep(1)
    print("Dwa")


def main():
    for z in range(3):
        count()

if __name__ == '__main__':

    s = time.perf_counter()
    main()
    # asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} wykonało się {elapsed:0.2f} sek.")
