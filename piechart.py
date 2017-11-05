import matplotlib.pyplot as plt

# def create_pie_chart(emotions):
    # labels = []
    # sizes = []
    # for k,v in emotions.iteritems():
    #     labels.append(k)
    #     sizes.append(v)
    # explode = (0,0,0,0)
    #
    # fig1, ax1 = plt.subplots()
    # ax1.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    # ax1.axis('equal')
    # plt.show()

labels = ['Anger', 'Happy', 'Sad', 'Excited', 'Mad', 'Glad']
sizes = [20, 17, 25, 10, 12, 16]
explode = (0,0,0,0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
