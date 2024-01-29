from transformers import BertTokenizer, BertForSequenceClassification
import pandas as pd
from sklearn.metrics import accuracy_score
import numpy as np

finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')

labels = {0:'neutral', 1:'positive',2:'negative'}

finance_news = pd.DataFrame({
    'headline':['The stock market is going up today',
                'The stock market is going down today',
                'The stock market is going sideways today'],
    'sentiment':[1, 2, 0]
})


X = finance_news['headline'].to_list()
y = finance_news['sentiment'].to_list()

sent_val = list()
for x in X:
    inputs = tokenizer(x, return_tensors="pt", padding=True)
    outputs = finbert(**inputs)[0]
    logits = outputs.detach().numpy()
    prediction = np.argmax(logits, axis=1).flatten()
    val = labels[np.argmax(outputs.detach().numpy())]
    print(x, '----', val)
    print('#######################################################')    
    sent_val.append(prediction[0])

print(accuracy_score(y, sent_val))