from app import app, app_routes
from app.data import constants
from app.exception import error_handler
from argparse import ArgumentParser


def get_command_line_arguments():
    parser = ArgumentParser()
    parser.add_argument("--ip", dest="ip", help="application server ip", default=constants.app_server_ip)
    parser.add_argument("--port", dest="port", help="application server port", default=constants.app_server_port)
    return parser.parse_args()


if __name__ == "__main__":
    args = get_command_line_arguments()
    app.run(debug=True, host=args.ip, port=args.port)
