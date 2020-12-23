import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.rcParams["font.sans-serif"] = "Microsoft Yahei"
    labels = ["食", "衣", "住", "行", "育", "樂"]
    values = [9000, 1200, 7000, 500, 550, 600]
    plt.pie(values, labels = labels, autopct = "%1.1f%%")
    plt.axis("equal")
    plt.show()