import sys
import requests
import json
import chardet
import matplotlib
import numpy as np

from ui.weather import Ui_Dialog
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRegExp
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QGridLayout, QAbstractItemView, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QIcon

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# 创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self):
        # 第一步：创建一个创建Figure
        self.fig = Figure()
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot()

    # # 第四步：就是画图，【可以在此类中画，也可以在其它类中画】
    def plot_sin(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)

    def plot_cos(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)


class SortFilterProxyModel(QSortFilterProxyModel):

    def __init__(self, *args, **kwargs):
        super(SortFilterProxyModel, self).__init__(*args, **kwargs)
        self.setFilterRole(Qt.ToolTipRole)  # 根据Qt.ToolTipRole角色过滤
        self._model = QStandardItemModel(self)
        self.setSourceModel(self._model)

    def append_row(self, item):
        self._model.appendRow(item)

    def set_filter(self, _):
        # 过滤
        # self.sender()#发送者
        # 获取上一个下拉框中的item_code
        item_code = self.sender().currentData(Qt.ToolTipRole)
        if not item_code:
            return
        if item_code.endswith("0000"):  # 过滤市
            self.setFilterRegExp(QRegExp(item_code[:-4] + "\d\d00"))
        elif item_code.endswith("00"):  # 过滤市以下
            self.setFilterRegExp(QRegExp(item_code[:-2] + "\d\d"))


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.tf = MyFigure()
        self.ui_setting()
        # self.mf.plot_sin()
        # self.plotcos()
        # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        self.gridlayout = QGridLayout(self.ui.groupBox_2)  # 继承容器groupBox
        # self.gridlayout.addWidget(self.mf, 0, 1)

        self.init_model()
        self.init_signal()
        self.init_data()
        self.query_weather()

    # def plot_cos(self):
    #     t = np.arange(0.0, 5.0, 0.01)
    #     s = np.cos(2 * np.pi * t)
    #     self.mf.axes.plot(t, s)
    #     self.mf.fig.suptitle("cos")
    def ui_setting(self):
        # self.setWindowIcon(QIcon("resource/cloud_32.ico"))
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        font = self.ui.tableWidget.horizontalHeader().font()
        font.setBold(True)
        self.ui.tableWidget.horizontalHeader().setFont(font)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.resText.setFont(QFont("Microsoft YaHei", 10))
        self.ui.resText.setReadOnly(True)
        self.setFixedSize(812, 568)

    def init_model(self):
        self.province_model = SortFilterProxyModel(self)
        self.city_model = SortFilterProxyModel(self)
        self.county_model = SortFilterProxyModel(self)
        self.ui.province_box.setModel(self.province_model)
        self.ui.city_box.setModel(self.city_model)
        self.ui.county_box.setModel(self.county_model)

    def init_signal(self):
        self.ui.province_box.currentTextChanged.connect(self.city_model.set_filter)
        self.ui.city_box.currentTextChanged.connect(self.county_model.set_filter)

    def init_data(self):
        datas = open("data/CityData.json", "rb").read()
        encoding = chardet.detect(datas) or {}
        datas = datas.decode(encoding.get("encoding", "utf-8"))
        datas = json.loads(datas)
        for data in datas:
            item_code = data.get("item_code")
            item_name = data.get("item_name")
            item = QStandardItem(item_name)
            item.setData(item_code, Qt.ToolTipRole)
            if item_code.endswith("0000"):
                self.province_model.append_row(item)
            elif item_code.endswith("00"):
                self.city_model.append_row(item)
            else:
                self.county_model.append_row(item)

    def query_weather(self):
        city_name = self.ui.city_box.currentText()
        city_code = self.get_code(city_name)
        if city_code:
            res_url = "http://t.weather.itboy.net/api/weather/city/{0}".format(city_code)
            res = requests.get(res_url)
            # with open('weather.json', "w", encoding="utf-8") as wfp:
            #     json.dump(res.json(), wfp, ensure_ascii=False)
            msg = res.json()
            if msg.get("status") == 200:
                weather_msg = "City:{0}\nDate:{1}\nWeather:{2}\nPM2.5:{3}\nPM10:{4}\nQuality:{5}\nTemperature:{6}℃\nHmidity:{7}\nWind Force:{8}\nGanmao:{9}\nNotice:{10}".format(
                    msg['cityInfo']['city'],
                    msg['data']['forecast'][0]['ymd'],
                    msg['data']['forecast'][0]['type'],
                    int(msg['data']['pm25']),
                    int(msg['data']['pm10']),
                    msg['data']['quality'],
                    msg['data']['wendu'],
                    msg['data']['shidu'],
                    msg['data']['forecast'][0]['fl'],
                    msg['data']["ganmao"],
                    msg['data']['forecast'][0]['notice'],
                )
                forecasts = msg["data"]["forecast"]
                self.ui.tableWidget.setRowCount(0)
                for data in forecasts:
                    row = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.insertRow(row)
                    items = [data["date"], data["type"], data["high"], data["low"], data["sunrise"], data["sunset"],
                             str(data["aqi"]), data["fx"],
                             data["fl"], data["notice"]]
                    for col in range(len(items)):
                        item = QTableWidgetItem(items[col])
                        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        self.ui.tableWidget.setItem(row, col, item)
                self.high_temp, self.low_temp, self.date = self.get_temp(forecasts)
                self.plot_temp()
                self.tf.draw()
                self.tf.flush_events()
            else:
                weather_msg = "Query weather fail, please try again later!"
            self.ui.resText.setText(weather_msg)
        else:
            self.ui.resText.setText("This city does not have weather data!")

    def plot_temp(self):
        # tf = MyFigure()
        self.tf.axes.clear()
        self.tf.axes.plot(self.date, self.high_temp, self.low_temp, marker="o")
        # tf.axes.axis([1, 16, -20, 20])
        for a, b in zip(self.date, self.high_temp):
            self.tf.axes.text(a, b + 0.5, '%d' % b, ha='center', va='bottom', fontsize=7)
        for a, b in zip(self.date, self.low_temp):
            self.tf.axes.text(a, b + 0.5, '%d' % b, ha='center', va='bottom', fontsize=7)
        # tf.axes.grid()
        self.gridlayout.addWidget(self.tf)

    def get_code(self, city_name):
        # city_id = {"北京": "101010100", "上海": "101020100", "武汉": "101200101", "成都": "101270101", "西安": "101110101",
        #            "广州": "101280101", "深圳": "101280601"}
        with open("data/CityCode.json", encoding="utf-8") as ccfp:
            citys = json.load(ccfp)
            for city in citys:
                if city["city_name"] == city_name[:-1] or city["city_name"] == city_name:
                    return city.get("city_code")

    def get_temp(self, forecasts):
        def split_str(str_temp):
            length = len(str_temp)
            if length == 5:
                temp = int(str_temp[3])
            elif length == 7:
                temp = 0 - int(str_temp[4:6])
            else:
                if str_temp[3] == "-":
                    temp = 0 - int(str_temp[4])
                else:
                    temp = int(str_temp[3:5])
            return temp

        high_temp = []
        low_temp = []
        date = []
        for forecast in forecasts:
            high = forecast["high"]
            h = split_str(high)
            high_temp.append(h)
            low = forecast["low"]
            l = split_str(low)
            low_temp.append(l)
            date.append(forecast["date"])
        return high_temp, low_temp, date

    def clear_text(self):
        self.ui.resText.clear()
        self.ui.tableWidget.setRowCount(0)


if __name__ == "__main__":
    with open("qss/Ubuntu.qss") as qssf:
        qss = qssf.read()
    app = QApplication(sys.argv)
    app.setStyleSheet(qss)
    dlg = MainDialog()

    dlg.show()
    sys.exit(app.exec_())
