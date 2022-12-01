from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar

from time import strftime

app = Flask(__name__, static_folder="templates")

timeList = [strftime('%H:%M:%S'), strftime('%H:%M:%S'), strftime('%H:%M:%S'), strftime('%H:%M:%S'), strftime('%H:%M:%S'), strftime('%H:%M:%S')]
def bar_base() -> Bar:
    timeIndex = strftime('%H:%M:%S')
    timeList.pop(0)
    timeList.append(timeIndex)
    c = (
        Bar()
        .add_xaxis(timeList)
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        #.add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    app.run()