import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from tqdm import tqdm
import os
import sys
import pandas as pd
import pickle

dom = sys.argv[1]

# Set device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Load model and tokenizer
model_path = f"model_weights/FlanT5_DST_models/{dom}/model"
tokenizer_path = f"model_weights/FlanT5_DST_models/{dom}/tokenizer"  # Path to the local tokenizer directory

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

# # Main execution
# if __name__ == "__main__":
    # Sample list of 20 inputs
data = pickle.load(open(f"domain_dst_test_data/{dom}.pkl", "rb"))
sample_inputs = list(data['prompts'])

sample_inputs = [f"Track the dialogue states related to the {dom} domain in the following conversation:\n\n{i}" for i in sample_inputs]

# for i in range(2):
#     print(sample_inputs[i])
#     print()

# # Perform batched inference
predictions = batched_inference(model, tokenizer, sample_inputs, batch_size)


dial_ids = data['diag_id']
conv_idxs = data['conv_idx']

import pickle
with open(f'domain_dst_results/{dom}_flanT5_dst.pickle', 'wb') as file:
    pickle.dump({"responses":predictions, "diag_id": dial_ids,"conv_idx": conv_idxs}, file)


# # Print results
# print("\nResults:")
# count = 0
# for input_text, prediction in zip(sample_inputs, predictions):
#     count += 1
#     print(count)
#     print(f"\nInput: {input_text}")
#     print(f"Prediction: {prediction}")
#     print("-" * 100)

# print("Inference completed.")