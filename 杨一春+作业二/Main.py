import keras
import Save
import Load
import MyUtil
import DenseModel
import ConvModel

'''
#已将数据集通过pickle打包为文件，直接load即可
Save.SaveImageAsPk('train')
Save.SaveImageAsPk('test')
Save.SaveLabelAsPk('test')
Save.SaveLabelAsPk('train')
'''

(raw_train_image, raw_train_label) = Load.load_train()
(raw_test_image, raw_test_label) = Load.load_test()

My_model = DenseModel.BuildDenseModel()
(train_image, train_label) = DenseModel.ProcessDataWithDense(raw_train_image, raw_train_label)
(test_image, test_label) = DenseModel.ProcessDataWithDense(raw_test_image, raw_test_label)

'''
My_model = ConvModel.BuildConvModel()
(train_image, train_label) = ConvModel.ProcessDataWithConv2D(raw_train_image, raw_train_label)
(test_image, test_label) = ConvModel.ProcessDataWithConv2D(raw_test_image, raw_test_label)
'''


My_model.summary()

My_model.fit(train_image, train_label, batch_size=64, epochs=5, validation_data=(test_image, test_label))


score = My_model.evaluate(test_image, test_label, verbose=0)
print('Total loss:', score[0])
print('Accuracy:', score[1])

result = My_model.predict_classes(test_image)

tru = 0
for i in result == raw_test_label:
    if i:
        tru += 1
print('True: ', tru)
print('False: ', result.shape[0] - tru)






