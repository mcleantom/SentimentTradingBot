from transformers import BertTokenizer, BertForSequenceClassification
import pandas as pd
from sklearn.metrics import accuracy_score
import numpy as np

finbert = BertForSequenceClassification.from_pretrained('ProsusAI/finbert',num_labels=3)
tokenizer = BertTokenizer.from_pretrained('ProsusAI/finbert')

labels = {0:'positive', 1:'negative', 2:'neutral'}

finance_news = pd.DataFrame({
    'headline':['The stock market is going up today',
                'The stock market is going down today',
                'The stock market is going sideways today',
                'The stock market is neither going up nor down today'],
    'sentiment':[0, 1, 2, 2]
})


X = finance_news['headline'].to_list()
y = finance_news['sentiment'].to_list()

sent_val = list()
for x in X:
    inputs = tokenizer(x, return_tensors="pt", padding=True)
    logits = finbert(**inputs).logits
    prediction = np.argmax(logits.detach().numpy(), axis=1)
    print(f'logits: {logits}')
    val = labels[prediction[0]]
    print(x, '----', val)
    print('#######################################################')    
    sent_val.append(prediction[0])

print(f'y: {y}')
print(f'sent_val: {sent_val}')

print(accuracy_score(y, sent_val))