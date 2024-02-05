import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

mpl.rcParams["font.size"] = 18

import matplotlib
import matplotlib as mpl

# sphinx_gallery_thumbnail_number = 2

# vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
#               "potato", "wheat", "barley"]
# farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
#            "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

fig, ax = plt.subplots()

vegetables = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
farmers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]

harvest = np.array([[0, 7.5, 2, 2.5, 3, 3.5, 4, 0, 7.5, 2, 2.5, 3, 3.5, 4],
                    [4.5, 5, 5.5, 6, 6.5, 7, 7.5, 0, 7.5, 2, 2.5, 3, 3.5, 4],
                    [8, 8.5, 9, 9.5, 10, 10.5, 11, 0, 7.5, 2, 2.5, 3, 3.5, 4],
                    [11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 2, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 2, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 2, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [8, 8.5, 9, 9.5, 10, 10.5, 11, 0, 7.5, 2, 2.5, 3, 3.5, 4],
                    ])

# harvest = np.array([[0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     [0, 0, 0, 2.5, 0, 2.5, 0, 0, 2.5, 0, 2.5, 0, 2.5, 0],
#                     ])


im = ax.imshow(X=harvest, cmap=plt.cm.get_cmap('gist_heat'))

for i, line in enumerate(ax.lines):
    ax.lines.pop(i)
    line.remove()

# ax.set_xticks(np.arange(len(farmers)), labels=farmers)
# ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)
ax.set_xticks(np.arange(14), labels=farmers)
ax.set_yticks(np.arange(14), labels=vegetables)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.tick_params(tick1On=False)

# plt.xticks([])

ax.legend()


fig.tight_layout()
plt.show()
