import pandas as pd

df = pd.read_csv('data.csv')

# helper function to get a single mean and std
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

# function that intake the required start, stop and step as well as the respective column name to produce a new csv file
def getMeansAndStdsForRange(start, stop, step, reference_column_name, target_column_name):
    mean_column_name ='mean of '+target_column_name
    std_column_name = 'std of ' +target_column_name
    indexes = []
    means = []
    stds = []
    for i in range(start, stop+1, step):
        if i == 0: continue
        mean, std = getMeanAndStd(i, reference_column_name, target_column_name)
        indexes.append(i)
        means.append(mean)
        stds.append(std)
    df = pd.DataFrame({reference_column_name:indexes,
                       mean_column_name:means,
                       std_column_name:stds})
    df.to_csv('mean_std_result.csv', index=False)
        

if __name__ == "__main__":
    mean, standard_deviation = getMeanAndStd(16, 'Duration', 'Pulse')
    print(mean)
    print(standard_deviation)
    getMeansAndStdsForRange(0, 40, 10, 'Duration', 'Pulse')
