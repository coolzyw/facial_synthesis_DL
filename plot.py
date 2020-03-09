import matplotlib.pyplot as plt


def read_data(filename):
    f = open(filename, "r")
    count = 0
    x = []
    y = []
    while True:
        line = f.readline()
        if not line:
            break
        separate = line.split(",")
        if len(separate) < 6:
            print(line)
            break
        loss = separate[5]
        index = loss.find(":")
        loss = float(loss[index+2:])
        if count % 20 == 0:
            x.append(count)
            y.append(loss)
        print("loss", loss)
        count += 1
    return x, y


def plot(x, y):
    plt.plot(x, y)
    plt.xlabel('iter')
    plt.ylabel('loss')
    plt.title("training loss vs iterations")
    plt.savefig("loss.png")


def main():
    filename = "plot.txt"
    x, y = read_data(filename)
    plot(x, y)


if __name__ == "__main__":
    main()