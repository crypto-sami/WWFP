from jinja2 import Environment, FileSystemLoader
import csv
from calculations import list_low, list_high, list_average, data

filename = 'output.html'
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("template.html")

results_filename = "templates/output.html"
results_template = environment.get_template("template.html")
context = {
    "tests": len(data),
    "data_low": list_low,
    "data_high": list_high,
    "data_avg": list_average,
}
with open(results_filename, mode="w", encoding="utf-8") as results:
    results.write(results_template.render(context))
    print(f"... wrote {results_filename}")




