import toml

# 创建一个字典来存储你的数据
data = {"auth.abc": "123"}

# 写入到一个toml文件中
with open("your_file.toml", "w") as toml_file:
    toml.dump(data, toml_file)
