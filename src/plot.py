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

def expenseHandler(values):
    labels = ["食", "衣", "住", "行", "育", "樂"]
    newValues = []
    newLabels = []
    for i in range(6):
        if values[i] != 0:
            newLabels.append(labels[i])
            newValues.append(values[i])
    return newValues, newLabels

def incomeHandler(values):
    labels = ["薪資", "獎金", "投資", "零用錢"]
    newValues = []
    newLabels = []
    for i in range(4):
        if values[i] != 0:
            newLabels.append(labels[i])
            newValues.append(values[i])
    return newValues, newLabels

def plotExpenseOrIncome(values, action, imgName):
    # draw pie chart
    plt.rcParams["font.size"] = 44.0
    plt.rcParams["font.sans-serif"] = "Microsoft Yahei"
    plt.rcParams["text.color"] = "#707070"
    if action == "支出":
        newValues, newLabels = expenseHandler(values)
    elif action == "收入":
        newValues, newLabels = incomeHandler(values)
    colors = determineColors(values, action)
    plt.figure(figsize=(20,15))
    plt.axis("equal")
    plt.title(action + "結構")
    plt.pie(newValues, labels = newLabels, colors = colors, pctdistance=0.85, autopct = "%1.1f%%")

    #draw circle
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.tight_layout()

    plt.savefig("./img/" + imgName, dpi = 30)

    # upload to imgur and get url
    CLIENT_ID = "b57c8df3844ca8d"
    PATH = "./img/" + imgName
    uploadedImg = pyimgur.Imgur(CLIENT_ID).upload_image(PATH, title = imgName)
    return uploadedImg.link

def plotRatio(expense, income, imgName):
    labels = ["支出", "收入"]
    values = [sum(expense), sum(income)]
    colors = ["#ff9b94", "#a1e6aa"]
    print(values)

    # draw image
    plt.rcParams["font.size"] = 44.0
    plt.rcParams["font.sans-serif"] = "Microsoft Yahei"
    plt.rcParams["text.color"] = "#707070"
    plt.figure(figsize=(20,15))
    plt.axis("equal")
    plt.title("收支比例")
    plt.pie(values, labels = labels, colors = colors, pctdistance=0.85, autopct = "%1.1f%%")

    #draw circle
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.tight_layout()

    plt.savefig("./img/" + imgName, dpi = 30)

    # upload to imgur and get url
    CLIENT_ID = "b57c8df3844ca8d"
    PATH = "./img/" + imgName
    uploadedImg = pyimgur.Imgur(CLIENT_ID).upload_image(PATH, title = imgName)
    return uploadedImg.link

def plotAll(expense, income, type, imgName):
    fontColor = "#707070"
    labels = ["薪資", "獎金", "投資", "零用錢", "食", "衣", "住", "行", "育", "樂"]
    values = income + expense

    plt.rcParams["font.size"] = 36.0
    plt.rcParams["font.sans-serif"] = "Microsoft Yahei"
    plt.rcParams["text.color"] = fontColor
    plt.rcParams["xtick.color"] = fontColor
    plt.rcParams["ytick.color"] = fontColor
    plt.rcParams["axes.labelcolor"] = fontColor
    plt.figure(figsize=(20,15))
    bars = plt.bar(labels, values, color = "#ffcccc")
    index = 0
    for bar in bars:
        if index < 4:
            bar.set_color("#d6f7a3")
        index += 1
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, "%d" % int(height), ha = "center", va = "bottom")
    plt.title("本" + type + "各項金額")
    # plt.xlabel("收支種類", labelpad = 25)
    # plt.ylabel("金額", labelpad = 10)
    plt.tick_params(axis = "x", which = "major", labelsize = 30, pad = 10)
    plt.tick_params(axis = "y", which = "major", labelsize = 30, pad = 5)
    plt.savefig("./img/" + imgName, dpi = 30)

    # upload to imgur and get url
    CLIENT_ID = "b57c8df3844ca8d"
    PATH = "./img/" + imgName
    uploadedImg = pyimgur.Imgur(CLIENT_ID).upload_image(PATH, title = imgName)
    return uploadedImg.link