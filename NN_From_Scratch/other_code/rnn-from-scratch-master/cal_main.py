from CalRNN import Model
import pickle
import numpy as np
cal_rnn = Model()

#先制作一个数据集合
file_training_data = open("calculator/cal_training.txt",'rb')
training_samples = pickle.load(file_training_data)

X_train = list()
y_train = list()
for i in range(len(training_samples)):
    abit = np.unpackbits(np.uint8(training_samples[i][0]))
    bbit = np.unpackbits(np.uint8(training_samples[i][1]))
    cbit = np.transpose(np.unpackbits(np.uint8(training_samples[i][2])))

    abbit = np.zeros((8,2),dtype=int)
    abbit[:,0] = abit
    abbit[:,1] = bbit
    X_train.append(abbit)
    y_train.append(cbit)
losses = cal_rnn.train(X_train, y_train, learning_rate=0.001, nepoch=10, evaluate_loss_after=1)