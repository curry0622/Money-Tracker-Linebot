import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pyimgur

def getColor(index):
    if index == 5:
        return "#f7b200"
    elif index == 4:
        return "#ffc933"
    elif index == 3:
        return "#ffd45c"
    elif index == 2:
        return "#ffe291"
    elif index == 1:
        return "#ffedba"
    elif index == 0:
        return "#e8e1cf"

def determineColors(values, action):
    colors = ["", "", "", "", "", ""]
    arr = np.array(values)
    sortedIndex = np.argsort(arr)
    if action == "支出":
        for i in range(6):
            color = getColor(i)
            index = sortedIndex[i]
            colors[index] = color
    elif action == "收入":
        for i in range(4):
            color = getColor(i)
            index = sortedIndex[i]
            colors[index] = color
    return colors

def plot(values, action, imgName):
    # draw pie chart
    plt.rcParams["font.size"] = 44.0
    plt.rcParams["font.sans-serif"] = "Microsoft Yahei"
    if action == "支出":
        newValues, newLabels, separate = expenseHandler(values)
    elif action == "收入":
        newValues, newLabels, separate = incomeHandler(values)
    colors = determineColors(values, action)
    plt.figure(figsize=(20,15))
    plt.axis("equal")
    plt.pie(newValues, labels = newLabels, colors = colors, explode = separate, autopct = "%1.1f%%")
    plt.savefig("./img/" + imgName, dpi = 30)

    # upload to imgur and get url
    CLIENT_ID = "b57c8df3844ca8d"
    PATH = "./img/" + imgName
    uploadedImg = pyimgur.Imgur(CLIENT_ID).upload_image(PATH, title = imgName)
    return uploadedImg.link

def expenseHandler(values):
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

def incomeHandler(values):
    labels = ["薪資", "獎金", "投資", "零用錢"]
    newValues = []
    newLabels = []
    separate = ()
    for i in range(4):
        if values[i] != 0:
            newLabels.append(labels[i])
            newValues.append(values[i])
            separate += (0.05, )
    return newValues, newLabels, separate

if __name__ == "__main__":
    values = [9000, 1200, 7000, 500, 550, 600]
    plotExpense(values, "test.png")