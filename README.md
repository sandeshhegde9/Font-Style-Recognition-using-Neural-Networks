# Font-Style-Recognition-using-Neural-Networks
This identifies the font style of a scanned document using Artificial Neural Networks.
# Preprocessing
1.py and 2.py are used to segment each character from image and convert this to feature matrix and labelling the vectors.
The results of these are stored in OCRDataset.obj and FontStyle.obj. They are the datasets for OCR and FontStyle Recognition respectively.

# Training and testing
OCRTrainer.py and FontStyletrainer.py are used to train the networks for OCR and Font Style Recognition respectibely. The data for these are stored in the serialized objects
