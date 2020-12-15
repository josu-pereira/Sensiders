from pyecharts.charts import Line
from pyecharts.charts import Bar
from pyecharts.charts import Gauge
from pyecharts.charts import Pie
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot as driver
import subprocess, sys, os


def abrirGrafico(abrirLocal=False):
    # pid = subprocess.Popen([sys.executable, "sendMessageFileSlack.py"])
    if abrirLocal:
        if sys.platform == 'linux':
            pid = subprocess.Popen(["xdg-open", "chart.png"])
        elif sys.platform == 'win32':
            pid = subprocess.Popen(["start", "chart.png"], shell=True)
        else:
            pid = subprocess.Popen(["open", "chart.png"])
    else:
        from tokenSlack import sendFile
        sendFile()


def linha(dados_x, dados_y, componente, temaEscuro=False, suavidade=False, abrir_local=False):
    if (temaEscuro):
        line = Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    else:
        line = Line(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))

    line.add_xaxis(xaxis_data=dados_x)
    line.add_yaxis(series_name=componente, y_axis=dados_y, symbol="emptyCircle", is_smooth=suavidade)
    line.set_global_opts(title_opts=opts.TitleOpts(title="Uso de " + componente + " recente"))

    make_snapshot(driver, line.render("chart.html"), "chart.png")

    abrirGrafico(abrir_local)
    return 0


def linhaDuplo(dados_x, dados_y, componente, labels_y, temaEscuro=False):
    if (temaEscuro):
        line = Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    else:
        line = Line(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))

    line.add_xaxis(xaxis_data=dados_x[0])
    line.add_yaxis(series_name=labels_y[0], y_axis=dados_y[0])
    line.add_yaxis(series_name=labels_y[1], y_axis=dados_y[1])
    line.set_global_opts(title_opts=opts.TitleOpts(title="Uso de " + componente + " recente"))

    make_snapshot(driver, line.render("chart.html"), "chart.png")

    abrirGrafico()
    return 0


def barra(dados_x, dados_y, componente, temaEscuro=False):
    if (temaEscuro):
        bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    else:
        bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))

    bar.add_xaxis(dados_x)
    bar.add_yaxis(componente, dados_y)
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Uso de " + componente + " recente"))

    make_snapshot(driver, bar.render("chart.html"), ("chart.png"))

    abrirGrafico()
    return 0


def gauge(dados, componente, metrica, temaEscuro=False, abrir_local=False):
    if (temaEscuro):
        gauge = Gauge(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    else:
        gauge = Gauge(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))

    gauge.add('', [(componente, dados)], start_angle=190, end_angle=-10,
              title_label_opts=opts.GaugeTitleOpts(font_size=28, color=("white" if temaEscuro else "black")),
              detail_label_opts=opts.GaugeDetailOpts(font_size=36, offset_center=[0, "25%"],
                                                     formatter=(str(dados) + str(metrica)),
                                                     color=("white" if temaEscuro else "black")))
    gauge.set_global_opts(title_opts=opts.TitleOpts(title="Uso de " + componente))

    make_snapshot(driver, gauge.render("chart.html"), "chart.png")

    abrirGrafico(abrir_local)
    return 0


def pizza(info, componente, metrica="%", temaEscuro=False):
    if (temaEscuro):
        pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    else:
        pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))

    pie.add(series_name=componente, data_pair=info)
    pie.set_global_opts(title_opts=opts.TitleOpts(title="Média de uso de " + componente))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} " + metrica))

    make_snapshot(driver, pie.render("chart.html"), "chart.png")

    abrirGrafico()
    return 0


def donut(info, componente, metrica="%", temaEscuro=False):
    if (temaEscuro):
        donut = Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    else:
        donut = Pie(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))

    donut.add(series_name=componente, data_pair=info, radius=["40%", "70%"])
    donut.set_global_opts(title_opts=opts.TitleOpts(title="Média de uso de " + componente))
    donut.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} " + metrica))

    make_snapshot(driver, donut.render("chart.html"), "chart.png")

    abrirGrafico()
    return 0


if __name__ == "__main__":
    print("Veja nossos gráficos!")
    li = input("Grafico de linha? [y/n] ")
    li = True if li.lower() == "y" else False
    lidu = input("Grafico de linha duplo? [y/n] ")
    lidu = True if lidu.lower() == "y" else False
    ba = input("Grafico de barra? [y/n] ")
    ba = True if ba.lower() == "y" else False
    ga = input("Grafico de gauge? [y/n] ")
    ga = True if ga.lower() == "y" else False
    pi = input("Grafico de pizza? [y/n] ")
    pi = True if pi.lower() == "y" else False
    do = input("Grafico de donut? [y/n] ")
    do = True if do.lower() == "y" else False
    if li:
        dark = input("Grafico de linha em modo escuro? [y/n] ")
        dark = True if dark.lower() == "y" else False
        if not dark:
            linha(["seg", "ter", "qua", "qui", "sex", "sab", "dom"], [5, 20, 36, 49, 77, 100, 66], "CPU")
        else:
            linha(["seg", "ter", "qua", "qui", "sex", "sab", "dom"], [5, 20, 36, 49, 77, 100, 66], "CPU", True)
    if lidu:
        dark = input("Grafico de linha duplo em modo escuro? [y/n] ")
        dark = True if dark.lower() == "y" else False
        if not dark:
            linhaDuplo()
        else:
            linhaDuplo(True)
    if ba:
        dark = input("Grafico de barra em modo escuro? [y/n] ")
        dark = True if dark.lower() == "y" else False
        if not dark:
            barra()
        else:
            barra(True)
    if ga:
        dark = input("Grafico de gauge em modo escuro? [y/n] ")
        dark = True if dark.lower() == "y" else False
        if not dark:
            gauge()
        else:
            gauge(True)
    if pi:
        dark = input("Grafico de pizza em modo escuro? [y/n] ")
        dark = True if dark.lower() == "y" else False
        if not dark:
            pizza()
        else:
            pizza(True)
    if do:
        dark = input("Grafico de donut em modo escuro? [y/n] ")
        dark = True if dark.lower() == "y" else False
        if not dark:
            donut()
        else:
            donut(True)