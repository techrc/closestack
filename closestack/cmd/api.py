from wsgiref import simple_server

from closestack.api import app


def main():
    # server
    host, port = "", 9099
    application = app.setup_app()
    server = simple_server.make_server(host, port, application)
    print("======== running server at {}:{} ========".format(host, port))
    server.serve_forever()


if __name__ == "__main__":
    main()
