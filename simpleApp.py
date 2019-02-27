from flask import Flask
import sys
import optparse

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world from Python & Docker!"

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python simpleapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()

    if args.port == None:
        print("Missing required argument: -p/--port")
        sys.exit(1)

    #Run the application
    app.run(host='0.0.0.0', port=int(args.port), debug=False)