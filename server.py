import etcd
import time


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    client = etcd.Client(host='127.0.0.1', port=2379)
    client.set('/nodes/n1', 1, ttl=30)
    client.set('/nodes/n2', 2, ttl=30)
    client.set('/nodes/n3', 3, ttl=30)

    print("service registered")

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print("service unregistered")


if __name__ == '__main__':
    serve()
