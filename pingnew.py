from flask import Flask
import subprocess
app = Flask(__name__)

@app.route("/")
def ping():
    data = (subprocess.check_output(["ping", "-c3", "-q", "192.168.111.100"]))
    data_crap = data.split('\n')
    # data = data.strip(data_crap[0])
    # data = data.strip(data_crap[1])
    # data = data.strip(data_crap[2])
    # data2 = data.strip(data_crap[3])
    return data_crap[3]
if __name__ == "__main__":
    app.run(host='0.0.0.0')
