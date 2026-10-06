def telemetry_generator(data):
    for value in data:
        yield value

def recursive_abnormal(data, index=0):
    if index >= len(data):
        return 0

    count = 1 if data[index] > 100 else 0

    return count + recursive_abnormal(data, index + 1)