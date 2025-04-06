# Jupyter Notebook(.ipynb) 파일을 Python(.py) 파일로 변환

import nbformat
from nbconvert import PythonExporter

def convert_ipynb_to_py(ipynb_path, py_path):
    with open(ipynb_path, 'r', encoding='utf-8') as f:
        nb_node = nbformat.read(f, as_version=4)

    exporter = PythonExporter()
    body, _ = exporter.from_notebook_node(nb_node)

    with open(py_path, 'w', encoding='utf-8') as f:
        f.write(body)

# 사용 예시
convert_ipynb_to_py("main.ipynb", "main.py")
