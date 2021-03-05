import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

fasion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fasion_mnist.load_data()

class_names = ['T-shirts/top', 'Trouser', 'Pullover', 'Dress', 
                'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# plt.figure()
# plt.imshow(train_images[0])
# plt.colorbar()
# plt.grid(False) #기본값은 false로 지정되어있어서 
# plt.show()

train_images = train_images / 255.0
test_images = test_images / 255.0
plt.figure(figsize=(10, 10))

# for i in range(25):
#     plt.subplot(5, 5, i+1)  # 5x5 plot 생성, 각각의 번호는 i+1
#     plt.xticks([])  #x축에 쓰이는 값(아무것도 안쓰이게 [])
#     plt.yticks([])
#     plt.imshow(train_images[i], cmap=plt.cm.binary) # train_images를 출력하는데 흑백으로.
#     plt.xlabel(class_names[train_labels[i]]) #x라벨에 이름적기
# plt.show()

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)), 
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\n테스트 정확도:', test_acc)

predictions = model.predict(test_images)
pp = np.argmax(predictions[0])
print(pp)
print(test_labels)