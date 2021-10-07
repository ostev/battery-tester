from statistics import mean
import sys
import matplotlib.pyplot as plot
import numpy

filenames = \
    [ "data/run_1" 
    , "data/run_2"
    , "data/run_3"
    # , "data/run_4"
    # , "data/run_5"
    # , "data/run_6"
    ]

data = []

i = 0
for filename in filenames:
    data_y = []
    data_x = []

    file = open(filename, "r")
    lines = file.read().split("\n")

    file.close()

    j = 0
    for line in lines:
        if line != "":
            data_y.append(float(line))
            data_x.append(j * 30)
            j += 1

    
    i += 1

    data.append((data_x, data_y))

smallest_dataset_size = 0

for dataset in data:
    # print(len(dataset[0]))
    if smallest_dataset_size == 0:
        smallest_dataset_size = len(dataset[0])
        # print(smallest_dataset_size)
    elif len(dataset[0]) < smallest_dataset_size:
        # print(len(dataset[0]))
        smallest_dataset_size = len(dataset[0])

normalised_data = []

for dataset in data:
    normalised_data.append((dataset[0][0:smallest_dataset_size], dataset[1][0:smallest_dataset_size]))

# def average_dataset(i, dataset_1, dataset_2):
#     # print(dataset_2[1][i])
#     # print(mean([dataset_1[1][i], dataset_2[1][i]]))
#     return mean([dataset_1[1][i], dataset_2[1][i]])

# def averaged_data(data_1, data_2): 
#     data = []
    
#     j = 0

#     for dataset in data_1:
#         averaged_dataset = []

#         for (i, x) in enumerate(dataset[1]):
#             averaged_dataset.append(average_dataset(i, dataset, data_2[j]))

#         print((averaged_dataset))

#         data.append((data_1[0], averaged_dataset))
#         j += 1

#     return data

# # print(len(normalised_data[0:3]))
# final_data = averaged_data(normalised_data[0:3], normalised_data[3:6]) if len(sys.argv) == 2 and sys.argv[1] == "--averaged" else normalised_data

final_data = normalised_data

figure, axis = plot.subplots()

def get_brand_name(run: int) -> str:
    if run == 3:
        return "Chevron"
    elif run == 2:
        return "Energizer Max Plus"
    elif run == 1:
        return "Eveready Gold"
    else:
        return get_brand_name(run - 3)

j = 1
for run in final_data:
    label = get_brand_name(j)
    axis.plot(run[0], run[1], label=label) 
    j += 1

axis.set_xlabel("Time (seconds)")
axis.set_ylabel("Voltage (volts)")
axis.set_title("AAA Battery Voltage Over Time, Organised by Brand")
axis.legend()

figure.savefig("graph.png", format="png")
figure.savefig("graph.svg", format="svg")

# Print hourly reports
def chunk(lst, n):
    return zip(*[iter(lst)]*n)

chunked = []

for dataset in normalised_data:
    chunked.append(list(chunk(dataset[1], 240))) # Seperates into 2-hour chunks

report_data = []

for dataset in chunked:
    dataset_report = []
    for chunk in dataset:
        dataset_report.append(mean(chunk))
    
    report_data.append(dataset_report)

report = "# Recorded Data (every 2 hours)\n\n"

k = 1
for dataset in report_data:
    report += "## " + get_brand_name(k) + "\n" + "\n"
    for item in dataset:
        report += str(item) + "\n"
    report += "\n"
    k += 1

print(report)

file = open("log.txt", "w")
file.write(report)
file.close()