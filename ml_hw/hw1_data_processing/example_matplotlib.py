import example_matplotlib.pyplot as plt
import example_numpy as np
import datetime as dt

np.random.seed(1)

STANDARD_SIZE = 3000

f, axs = plt.subplots(2, 2, figsize=(12, 8))
f.suptitle('Plot examples', fontsize=20)

ax1 = axs[0, 0]
ax2 = axs[0, 1]
ax3 = axs[1, 0]
ax4 = axs[1, 1]

x1, y1 = np.random.multivariate_normal([20, 10], [[1, 0.7], [0.7, 1]], STANDARD_SIZE).T
ax1.scatter(x1, y1, c='lightblue', edgecolors='black')
ax1.set_title('Scatter plot example', )
ax1.set_xlim([17, 23])
ax1.set_ylim([5, 14])

bar_bins = 40
y2 = np.random.geometric(p=0.1, size=STANDARD_SIZE)
ax2.hist(y2, bins=bar_bins, color='red')
ax2.set_title('Hist plot example', )

x3 = np.linspace(0.01, 6)
y3_x = np.array([np.log(x) for x in x3])
y3_2x = np.array([np.log(2 * x) for x in x3])
ax3.plot(x3, y3_x, color='black', label='$\itlog(x)$')
ax3.plot(x3, y3_2x, color='red', label='$\itlog(2x)$')
ax3.set_title('Line plot example', )
ax3.set_xlim([-0.5, 6.5])
ax3.set_ylim([-4, 3])
ax3.legend(shadow=True)

x4 = [dt.datetime.strftime(dt.datetime(year=2021, month=1, day=1) +
                           dt.timedelta(days=d), '%Y-%m-%d') for d in range(14)]
y4 = [np.random.normal(5, 1) for x in x4]
ax4.bar(x4, y4)
ax4.set_title('Bar plot example', )
plt.xticks(rotation=90)

f.set_tight_layout(True)
