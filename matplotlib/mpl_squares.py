import matplotlib.pyplot



input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
matplotlib.pyplot.plot(input_value,squares,linewidth=5)
matplotlib.pyplot.xlabel('Value',fontsize=14)
matplotlib.pyplot.title('Squares of Value',fontsize=24)

matplotlib.pyplot.tick_params(axis='both',labelsize=14)

matplotlib.pyplot.show()
