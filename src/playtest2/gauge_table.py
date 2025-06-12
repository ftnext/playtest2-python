"""https://github.com/getgauge/gauge-python/blob/v0.4.10/tests/test_python.py#L185-L193"""


class ProtoTable:
    def __init__(self, table_dict):
        self.headers = ProtoRow(table_dict["headers"]["cells"])
        self.rows = [ProtoRow(row["cells"]) for row in table_dict["rows"]]


class ProtoRow:
    def __init__(self, cells):
        self.cells = cells
