from app.client.client import Client
from app.server.server import Server


def main():
    message = input("Что хотите запустить? (server/client): ")
    if message in ("server", "s"):
        with Server() as server:
            server.run()
    elif message in ("client", "c"):
        with Client() as client:
            try:
                client.run()
            except (ConnectionAbortedError, ValueError):
                pass
    else:
        print("Некорректные данные.")


if __name__ == "__main__":
    main()
