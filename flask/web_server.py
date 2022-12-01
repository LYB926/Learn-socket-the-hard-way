from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Line

from time import strftime

app = Flask(__name__, static_folder="templates")

timeList = [strftime('%H:%M:%S') for __ in range(32)]
dataList = [0 for _ in range(32)]

def Line_base() -> Line:
    timeIndex = strftime('%H:%M:%S')
    timeList.pop(0)
    timeList.append(timeIndex)
    dataNext = randrange(0, 20)
    dataList.pop(0)
    dataList.append(dataNext)
    c = (
        Line()
        .add_xaxis(timeList)
        .add_yaxis("VCC", dataList)
        #.add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="VCC Monitor", subtitle=""))
    )
    return c


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/updateChart")
def get_Line_chart():
    c = Line_base()
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    app.run()