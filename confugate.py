import yaml
from jinja2 import Template

with open('data.yml') as data_file:
    config_data = yaml.load(data_file, Loader=yaml.FullLoader)

with open('vhosts.j2') as template_file:
    template_html = template_file.read()

template = Template(template_html)
vhosts_conf = template.render(config_data)

with open('vhosts.conf', 'w') as vhosts:
    vhosts.write(vhosts_conf)
print("done")
