# 功能：从CSV文件读取数据
import csv


def from_csv():
    filename='C:\\Users\\lw\\Desktop\\无线认证用户.csv'
    with open(filename) as f:
        reader = csv.reader(f)
    return reader
