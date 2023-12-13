from bob_telegram_tools.bot import TelegramBot
import matplotlib.pyplot as plt

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop
import numpy as np

from bob_telegram_tools.keras import KerasTelegramCallback
from bob_telegram_tools.bot import TelegramBot

token = '6892868655:AAHYz80uP417eLmvbRf-iYZ1V7qsTVNw_hE'
user_id = int('1556120359')
bot = TelegramBot(token, user_id)

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')

print(plt)
bot.send_plot(plt)

# This method delete the generetad image
bot.clean_tmp_dir()


X = np.random.rand(1000, 100)
y = (np.random.rand(1000, 3) > 0.5).astype('float32')

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(100,)))
model.add(Dense(512, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

n_epochs = 3

bot = TelegramBot(token, user_id)

tl = KerasTelegramCallback(bot, epoch_bar=True, to_plot=[
    {
        'metrics': ['loss', 'val_loss']
    },
    {
        'metrics': ['acc', 'val_acc'],
        'title':'Accuracy plot',
        'ylabel':'acc',
        'ylim':(0, 1),
        'xlim':(1, n_epochs)
    }
])

history = model.fit(X, y,
                    batch_size=10,
                    epochs=n_epochs,
                    validation_split=0.15,
                    callbacks=[tl])