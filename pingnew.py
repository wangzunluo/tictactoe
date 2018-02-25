from flask import Flask
import subprocess
app = Flask(__name__)

def parseSummary(summary):
    splitSummary = summary.split(" = ")
    data = splitSummary[0].split("/")
    values = splitSummary[1].split("/")
    return [data, values]


@app.route("/")
def ping():
    data = (subprocess.check_output(["ping", "-c3", "-q", "192.168.111.100"]))
    data_crap = data.split('\n')
    # data = data.strip(data_crap[0])
    # data = data.strip(data_crap[1])
    # data = data.strip(data_crap[2])
    # data2 = data.strip(data_crap[3])
    parsedStrings = parseSummary(data)
    data = parsedStrings[0]
    values = parsedStrings[1]
    return render_template("pingpage.html", rtm = data[0], 
    rtmd = values[0], avg = data[1], avgv = values[1], max = data[2], 
    maxv = values[2], sd = data[3], sdv = values[3])
if __name__ == "__main__":
    app.run(host='0.0.0.0')
