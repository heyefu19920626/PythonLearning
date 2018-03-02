import matplotlib.pyplot as plt


x_vaules = list(range(1,1001))
y_values = [x**2 for x in x_vaules]
# plt.scatter(x_vaules,y_values,c=(1,0,0),edgecolor='green',s=40)
plt.scatter(x_vaules,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()

