import pandas as pd
import os

def split_csv_by_size(csv_path, output_dir, chunk_size_mb=10):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    chunk_size = chunk_size_mb * 1024 * 1024  # 字节
    base_name = os.path.splitext(os.path.basename(csv_path))[0]
    with open(csv_path, 'r', encoding='utf-8') as f:
        header = f.readline()
        part = 1
        out_file = open(os.path.join(output_dir, f"{base_name}_part{part}.csv"), 'w', encoding='utf-8')
        out_file.write(header)
        size = len(header.encode('utf-8'))
        for line in f:
            line_size = len(line.encode('utf-8'))
            if size + line_size > chunk_size:
                out_file.close()
                part += 1
                out_file = open(os.path.join(output_dir, f"{base_name}_part{part}.csv"), 'w', encoding='utf-8')
                out_file.write(header)
                size = len(header.encode('utf-8'))
            out_file.write(line)
            size += line_size
        out_file.close()
    print(f"{csv_path} 拆分完成，输出到 {output_dir}")

# 示例用法
csv_file = 'data/csv/train-00003-of-00004-df01a1242248f09b.csv'  # 替换为你的大csv文件路径
output_dir = 'split_csv'               # 拆分后输出目录
split_csv_by_size(csv_file, output_dir, chunk_size_mb=10)