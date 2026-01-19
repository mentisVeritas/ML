def normalization(num,data):
    data = sorted(data)
    return (num - data[0]) / (data[-1] - data[0])
