# first line: 94
@mem.cache
def get_data():
    data = load_svmlight_file("C:\\Users\\555\\Desktop\\22.txt")
    return data[0], data[1]
