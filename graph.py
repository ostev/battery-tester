import matplotlib.pyplot as plot
import numpy

filenames = ["data/run_1", "data/run_2", "data/run_3"] 

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
            j+=1

    
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

figure, axis = plot.subplots()

j = 1
for run in normalised_data:
    label = ""
    if j % 3 == 0:
        label = "Chevron"
    elif j % 2 == 0:
        label = "Energizer Max Plus"
    else:
        label = "Eveready Gold"
    axis.plot(run[0], run[1], label=label) 
    j += 1

axis.set_xlabel("Time (seconds)")
axis.set_ylabel("Voltage (volts)")
axis.set_title("AAA Battery Voltage Over Time, Organised by Brand")
axis.legend()

figure.savefig("graph.png", format="png")
