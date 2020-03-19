# this is a comment
'''and so is this'''
print("Hello World")  # todo take over the world
'''#todo gives a todo list '''
# several lines can be commented/uncommented with crlt+/

#%%
'''#%% gives structure, similar to matlab supported in spider and prof version? of PyCharm'''

print("Hello World")  # todo how to run just this line?
'''answer:alt+shift+e, however first turn off the windows shortcut for changing keyboard settings
  some guides say it should be crlt+shift+e '''
'''Settings > search for 'typing' > Advanced keyboard settings > Language > Bar options >
 Advanced Key Settings (tab) > Change Key Sequence (unclick the crlt+shift, alt+shift)'''


'''packages numpy gives a lot of matlab commands, if not already installed (numpy is, but matplotlib is not) 
open a command line type "conda install matplotlib", this installs it, but pycharm might need some help 
goto: file-> settings ->project: python-> python interpreter   there is a long list,  '''

import matplotlib.pyplot as plt
import numpy as np
x=2-3
#test

x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x ** 2, label='quadratic')
plt.plot(x, x ** 3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

# plt.plot(x, x, label='linear')

# plt.plot(x, x, label='linear')
# plt.plot(x, x ** 2, label='quadratic')
# plt.plot(x, x ** 3, label='cubic')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()
# plt.show()
#test change
# open("data.csv","r")
