from flask import render_template, request, Flask, send_from_directory
from uuid import uuid4

global name
name = ""


def roadreduce(inputData):
    """fuck"""
    inputData = inputData.split("\n")
    dataInput = len(inputData)

    # print("Have Read %d data" % dataInput)

    data = []
    data2 = []
    print(dataInput)
    # for i in inputData:
    #     tup = (int(i[1]), int(i[2]))
    #     if (inputData.index(i) >= 2):
    #         temp1 = data[-2]
    #         temp = data[-1]
    #         if((temp[0] - tup[0] < 2) and (temp[1] - tup[1] < 2) \
    #             and temp1[0] - tup[0] > 2 and temp1[1] - tup[1] > 2):
    #             del data[-1]
    #     data.append(tup)

    for i in inputData:
        # print(i)
        if i != "":
            ha = i.split()
            tup = (int(ha[0]), int(ha[1]))
            if (inputData.index(i) >= 2):
                temp1 = data2[-2]
                temp = data2[-1]
                if((temp[0] - tup[0] < 2) and (temp[1] - tup[1] < 2)):
                    del data2[-1]
            data2.append(tup)

    # print(data2)
    # print(len(data))

    result = []
    last = data2[0]
    for data in data2:
        maxTime = max(abs(last[0]-data[0]), abs(last[1] - data[1]))
        last = data
        result.append("%d %d %d" % (data[0], data[1], maxTime * 30+300))
    return result

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("pic2road.html")


@app.route('/data', methods=["POST"])
def dataDo():
    inputdata = request.form["data"]
    if inputdata:
        result = roadreduce(inputdata)
        global name
        name = str(uuid4())
        with open("data/%s.txt" % name, "w") as f:
            f.write("\n".join(result))
        return render_template("down.html", filename=name)
    else:
        return "NO DATA"


@app.route('/download/<ha>')
def dataput(ha):
    print(name)
    return send_from_directory("data", name+".txt")

app.run(port=1888, debug=True)


