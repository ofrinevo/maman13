# coding=utf-8
import sys

import client
import console
import server


def main():
    if len(sys.argv) < 2:
        print 'enter arg form console/server/client'
        return
    if sys.argv[1] == 'client':
        host, port = None, None
        if len(sys.argv) >= 4:
            host, port = sys.argv[2], sys.argv[3]
        client.run_client(host, port)
    elif sys.argv[1] == 'server':
        host, port = None, None
        if len(sys.argv) >= 4:
            host, port = sys.argv[2], sys.argv[3]
        server.run_server(host, port)
    elif sys.argv[1] == 'console':

        console.console_mode()
    else:
        print 'enter arg form console/server/client'
    return


if __name__ == "__main__":
    main()
