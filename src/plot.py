import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pyimgur

def determineColors(values):
    colors = ["", "", "", "", "", ""]
    arr = np.array(values)
    sortedIndex = np.argsort(arr)
    for index in sortedIndex:
        if(index == 5):
            colors[index] = "#fff1c7"
        elif(index == 4):
            colors[index] = "#ffe494"
        elif(index == 3):
            colors[index] = "#ffde7a"
        elif(index == 2):
            colors[index] = "#ffd861"
        elif(index == 1):
            colors[index] = "#ffce3b"
        elif(index == 0):
            colors[index] = "#ffc100"
    return colors

def plotExpense(values, imgName):
    # draw pie chart
    plt.rcParams["font.size"] = 44.0
    plt.rcParams["font.sans-serif"] = "Microsoft Yahei"
    newValues, newLabels, separate = valuesHandler(values)
    colors = determineColors(values)
    plt.figure(figsize=(20,15))
    plt.axis("equal")
    plt.pie(newValues, labels = newLabels, colors = colors, explode = separate, autopct = "%1.1f%%")
    plt.savefig("./img/" + imgName, dpi = 30)

    # upload to imgur and get url
    CLIENT_ID = "b57c8df3844ca8d"
    PATH = "./img/" + imgName
    uploadedImg = pyimgur.Imgur(CLIENT_ID).upload_image(PATH, title = "expense")
    return uploadedImg.link

def valuesHandler(values):
    labels = ["食", "衣", "住", "行", "育", "樂"]
    newValues = []
    newLabels = []
    separate = ()
    for i in range(6):
        if values[i] != 0:
            newLabels.append(labels[i])
            newValues.append(values[i])
            separate += (0.05, )
    return newValues, newLabels, separate

if __name__ == "__main__":
    # plt.rcParams["font.sans-serif"] = "Microsoft Yahei"
    # labels = ["食", "衣", "住", "行", "育", "樂"]
    # values = [9000, 1200, 7000, 500, 550, 600]
    # colors = ["#ffd754", "#ffe180", "#ffe89e", "#ffedb3", "#fff3cc", "#fff5d6"]
    # separate = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
    # plt.pie(values, labels = labels, colors = colors, explode = separate, autopct = "%1.1f%%")
    # plt.axis("equal")
    # plt.show()
    # plt.savefig("./img/test.png", dpi = 300)
    values = [9000, 1200, 7000, 500, 550, 600]
    plotExpense(values, "test.png")