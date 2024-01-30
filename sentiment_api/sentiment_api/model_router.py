from fastapi import APIRouter
from .config import APIConfig, SentimentModelConfig
from transformers import BertTokenizer, BertForSequenceClassification


def create_model_router(api_config: APIConfig) -> APIRouter:
    router = APIRouter()

    bert_model = BertForSequenceClassification.from_pretrained(api_config.sentiment_model.bert_model, num_labels=len(api_config.sentiment_model.encoding))
    tokenizer = BertTokenizer.from_pretrained(api_config.sentiment_model.bert_model)
    labels = api_config.sentiment_model.encoding

    @router.get("/")
    def root():
        return {"message": "Hello World"}
    
    @router.get("/predict")
    def predict(text: str):
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        logits = bert_model(**inputs).logits
        prediction = logits.detach().numpy().argmax(axis=1)
        return {"prediction": labels[prediction[0]]}

    return router