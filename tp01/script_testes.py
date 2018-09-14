import io
import plotly.offline as py
import plotly.graph_objs as go
import psutil
import subprocess
import time

path = "c:/Users/luigi/dev/pucminas/paa/tp01/"
greedy_exe = path + "greedy.exe"
dp_exe = path + "dp.exe"

days = [i for i in range(1, 22)]
dishes = [i for i in range(1, 51)]
budget = [i for i in range(0, 101)]

max_days = days[len(days) - 1]
max_dishes = dishes[len(dishes) - 1]
max_budget = budget[len(budget) - 1]

greedy_time = [0 for i in range(len(days))]
dp_time = [0 for i in range(len(days))]

greedy_mem = [0 for i in range(len(days))]
dp_mem = [0 for i in range(len(days))]

num_tests = 20

i = 0
# Variando quantidade de dias
for day in days:
    with open("inputs/{}_{}_{}.in".format(day, max_dishes, max_budget)) as input_file:
        start_time = time.time()
        with subprocess.Popen([greedy_exe], stdin=input_file, stdout=subprocess.PIPE) as p:
            mem = psutil.Process(p.pid).memory_info().rss
            p.wait()
            end_time = time.time();
            greedy_mem[i] = mem / 2 ** 20
            greedy_time[i] = end_time - start_time;
#    greedy_mem[i] /= num_tests
 #   greedy_time[i] /= num_tests
    i += 1


i = 0
for day in days:
    with open("inputs/{}_{}_{}.in".format(day, max_dishes, max_budget)) as input_file:
        start_time = time.time()
        with subprocess.Popen([dp_exe], stdin=input_file, stdout=subprocess.PIPE) as p:
            mem = psutil.Process(p.pid).memory_info().rss
            p.wait()
            end_time = time.time();
            dp_mem[i] = mem / 2 ** 20
            dp_time[i] = end_time - start_time;
  #  dp_mem[i] /= num_tests
   # dp_time[i] /= num_tests
    i += 1

# Tempo de execucao
trace_greedy = go.Scatter(
    x=days,
    y=greedy_time,
    name="Guloso"
)

trace_dp = go.Scatter(
    x=days,
    y=dp_time,
    name="Dinâmico"
)

data = [trace_greedy, trace_dp]
layout = go.Layout(
    xaxis=dict(
        title="Nº de dias",
        titlefont=dict(
            family="Arial, sans-serif",
            size=18,
        ),
    ),
    yaxis=dict(
        title="Tempo de execução (s)",
         titlefont=dict(
            family="Arial, sans-serif",
            size=18,
        ),
    )
)
figure = go.Figure(data=data, layout=layout)
py.plot(figure, filename=path + "outputs/days_exec_time.html")

# Consumo de memoria
trace_greedy = go.Scatter(
    x=days,
    y=greedy_mem,
    name="Guloso"
)

trace_dp = go.Scatter(
    x=days,
    y=dp_mem,
    name="Dinâmico"
)

data = [trace_greedy, trace_dp]
layout = go.Layout(
    xaxis=dict(
        title="Nº de dias",
        titlefont=dict(
            family="Arial, sans-serif",
            size=18,
        ),
    ),
    yaxis=dict(
        title="Consumo de memória (MB)",
         titlefont=dict(
            family="Arial, sans-serif",
            size=18,
        ),
    )
)
figure = go.Figure(data=data, layout=layout)
py.plot(figure, filename=path + "outputs/days_mem_usage.html")

# Variando quantidade de pratos
greedy_time = [0 for i in range(len(dishes))]
dp_time = [0 for i in range(len(dishes))]

greedy_mem = [0 for i in range(len(dishes))]
dp_mem = [0 for i in range(len(dishes))]

i = 0
for dish in dishes:
    with open("inputs/{}_{}_{}.in".format(max_days, dish, max_budget)) as input_file:
        start_time = time.time()
        with subprocess.Popen([greedy_exe], stdin=input_file, stdout=subprocess.PIPE) as p:
            mem = psutil.Process(p.pid).memory_info().rss
            p.wait()
            end_time = time.time();
            greedy_mem[i] = mem / 2 ** 20
            greedy_time[i] = end_time - start_time;
#    greedy_mem[i] /= num_tests
 #   greedy_time[i] /= num_tests
    i += 1


i = 0
for dish in dishes:
    with open("inputs/{}_{}_{}.in".format(max_days, dish, max_budget)) as input_file:
        start_time = time.time()
        with subprocess.Popen([dp_exe], stdin=input_file, stdout=subprocess.PIPE) as p:
            mem = psutil.Process(p.pid).memory_info().rss
            p.wait()
            end_time = time.time();
            dp_mem[i] = mem / 2 ** 20
            dp_time[i] = end_time - start_time;
#    dp_mem[i] /= num_tests
 #   dp_time[i] /= num_tests
    i += 1

# Tempo de execucao
trace_greedy = go.Scatter(
    x=dishes,
    y=greedy_time,
    name="Guloso"
)

trace_dp = go.Scatter(
    x=dishes,
    y=dp_time,
    name="Dinâmico"
)

data = [trace_greedy, trace_dp]
layout = go.Layout(
    xaxis=dict(
        title="Nº de pratos",
        titlefont=dict(
            family="Arial, sans-serif",
            size=18,
        ),
    ),
    yaxis=dict(
        title="Tempo de execução (s)",
         titlefont=dict(
            family="Arial, sans-serif",
            size=18,
        ),
    )
)
figure = go.Figure(data=data, layout=layout)
py.plot(figure, filename=path + "outputs/dishes_exec_time.html")

# Consumo de memoria
trace_greedy = go.Scatter(
    x=dishes,
    y=greedy_mem,
    name="Guloso"
)

trace_dp = go.Scatter(
    x=dishes,
    y=dp_mem,
    name="Dinâmico"
)

data = [trace_greedy, trace_dp]
layout = go.Layout(
    xaxis=dict(
        title="Nº de pratos",
        titlefont=dict(
            family="Arial, sans-serif",
            size=18,
        ),
    ),
    yaxis=dict(
        title="Tempo de execução (s)",
         titlefont=dict(
            family="Arial, sans-serif",
            size=18,
        ),
    )
)
figure = go.Figure(data=data, layout=layout)
py.plot(figure, filename=path + "outputs/dishes_mem_usage.html")


# Variando orcamento
greedy_time = [0 for i in range(len(budget))]
dp_time = [0 for i in range(len(budget))]

greedy_mem = [0 for i in range(len(budget))]
dp_mem = [0 for i in range(len(budget))]

i = 0
for b in budget:
    with open("inputs/{}_{}_{}.in".format(max_days, max_dishes, b)) as input_file:
        start_time = time.time()
        with subprocess.Popen([greedy_exe], stdin=input_file, stdout=subprocess.PIPE) as p:
            mem = psutil.Process(p.pid).memory_info().rss
            p.wait()
            end_time = time.time();
            greedy_mem[i] = mem / 2 ** 20
            greedy_time[i] = end_time - start_time;
#    greedy_mem[i] /= num_tests
 #   greedy_time[i] /= num_tests
    i += 1

        
i = 0
for b in budget:
    with open("inputs/{}_{}_{}.in".format(max_days, max_dishes, b)) as input_file:
        start_time = time.time()
        with subprocess.Popen([dp_exe], stdin=input_file, stdout=subprocess.PIPE) as p:
            mem = psutil.Process(p.pid).memory_info().rss
            p.wait()
            end_time = time.time();
            dp_mem[i] = mem / 2 ** 20
            dp_time[i] = end_time - start_time;
   # dp_mem[i] /= num_tests
  #  dp_time[i] /= num_tests
    i += 1

# Tempo de execucao
trace_greedy = go.Scatter(
    x=budget,
    y=greedy_time,
    name="Guloso"
)

trace_dp = go.Scatter(
    x=budget,
    y=dp_time,
    name="Dinâmico"
)

data = [trace_greedy, trace_dp]
layout = go.Layout(
    xaxis=dict(
        title="Orçamento",
        titlefont=dict(
            family="Arial, sans-serif",
            size=18,
        ),
    ),
    yaxis=dict(
        title="Tempo de execução (s)",
         titlefont=dict(
            family="Arial, sans-serif",
            size=18,
        ),
    )
)
figure = go.Figure(data=data, layout=layout)
py.plot(figure, filename=path + "outputs/budget_exec_time.html")

# Tempo de execucao
trace_greedy = go.Scatter(
    x=budget,
    y=greedy_mem,
    name="Guloso"
)

trace_dp = go.Scatter(
    x=budget,
    y=dp_mem,
    name="Dinâmico"
)

data = [trace_greedy, trace_dp]
layout = go.Layout(
    xaxis=dict(
        title="Orçamento",
        titlefont=dict(
            family="Arial, sans-serif",
            size=18,
        ),
    ),
    yaxis=dict(
        title="Tempo de execução (s)",
         titlefont=dict(
            family="Arial, sans-serif",
            size=18,
        ),
    )
)
figure = go.Figure(data=data, layout=layout)
py.plot(figure, filename=path + "outputs/budget_mem_usage.html")
