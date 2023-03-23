from jinja2 import Environment, FileSystemLoader
import csv
from calculations import high_score, data

filename = 'output.html'
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("results.html")

content = template.render(
    max_score=high_score(data, 1, 4)
)


with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
    print(f"... wrote {filename}")




