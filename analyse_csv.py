import pandas as pd

df = pd.read_csv('data.csv')

def getMeanAndStd(break_point, reference_column_name, target_column_name):
    time_series = df[reference_column_name]
    break_index = 0
    for i in range(len(time_series)):
        if time_series[i] >= break_point:
            break_index = i
            break
    break_index += 1

    mean = df[target_column_name][:break_index].mean()
    std = df[target_column_name][:break_index].std()
    return (mean, std)

if __name__ == "__main__":
    mean, standard_deviation = getMeanAndStd(16, 'Duration', 'Pulse')
    print(mean)
    print(standard_deviation)
