from transformers import PegasusTokenizer, PegasusForConditionalGeneration
import torch
import warnings
from transformers import logging as hf_logging

warnings.filterwarnings("ignore")
hf_logging.set_verbosity_error()


model_name = "google/pegasus-xsum"
tokenizer = PegasusTokenizer.from_pretrained(model_name)
#model = PegasusForConditionalGeneration.from_pretrained(model_name)
model=None

def summarize_text(text: str, min_length: int = 20, max_length: int = 60) -> str:
    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
    #summary_ids = model.generate(**tokens, min_length=min_length, max_length=max_length, num_beams=8, early_stopping=False)
    #summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    #return summary
    return "Summary feature temporarily disabled due to model loading issues."
