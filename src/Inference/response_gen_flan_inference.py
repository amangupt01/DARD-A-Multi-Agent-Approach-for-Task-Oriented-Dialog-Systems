import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from tqdm import tqdm
import os
import sys
import pandas as pd


# Set device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Load model and tokenizer - TODO
model_path = f"/path/to/your/trained Model"
tokenizer_path = f"/path/to/model/tokenizer"  # Path to the local tokenizer directory

# Ensure the paths exist
assert os.path.exists(model_path), f"Model path does not exist: {model_path}"
assert os.path.exists(tokenizer_path), f"Tokenizer path does not exist: {tokenizer_path}"

model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(device)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path, local_files_only=True)

# Batch size for inference
batch_size = 16

# Function for batched inference
def batched_inference(model, tokenizer, input_data, batch_size):
    results = []
    for i in tqdm(range(0, len(input_data), batch_size)):
        batch = input_data[i:i+batch_size]
        
        # Tokenize inputs
        encoded_inputs = tokenizer(batch, padding=True, truncation=True, return_tensors="pt").to(device)
        
        # Generate outputs
        with torch.no_grad():
            outputs = model.generate(**encoded_inputs, max_length=100)
        
        # Decode outputs
        decoded_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        
        results.extend(decoded_outputs)
    
    return results

## TODO - Update the path to the test data
data = pd.read_excel('/path/to/test/data', index_col=0)


sample_inputs = [i.replace("Now its your turn to answer, the following is the current conversation context:\n", "Track the dialogue states present in the following conversation:\n\n").replace("Answer: ", "") for i in list(data['prompts'])]

print("Number of inputs", len(sample_inputs))

predictions = batched_inference(model, tokenizer, sample_inputs, batch_size)


dial_ids = data['dialogue_id']
conv_idxs = data['conv_idx']

import pickle
with open(f'domain_res_gen_results/generic_model_flanT5_with_venues.pickle', 'wb') as file:
    pickle.dump({"responses":predictions, "diag_id": dial_ids,"conv_idx": conv_idxs}, file)

