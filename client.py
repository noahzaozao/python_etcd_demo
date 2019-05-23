import etcd


def run():
    client = etcd.Client(host='127.0.0.1', port=2379)

    try:
        client.read('/nodes')
        directory = client.get('/nodes')

        if directory and directory.children:
            for result in directory.children:
                print(str(result.key) + ': ' + str(result.value))

        result = client.read('/nodes/n1', wait=True)
        print(result)

    except etcd.EtcdKeyNotFound:
        print('error')


if __name__ == '__main__':
    run()



