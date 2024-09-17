from vllm import LLM, SamplingParams
import torch
import pickle
import sys
import pandas as pd


dom = sys.argv[1]

llm = LLM(model = f'model_weights/Response_gen_with_venues/Mistral7B/{dom}/model/epoch_10', tensor_parallel_size = torch.cuda.device_count())

sampling_params = SamplingParams(temperature=0.7, top_p=0.95, max_tokens=512)

data = pd.read_excel(f'test_data_with_venues/{dom}_test_updated.xlsx')

print(data.keys())
inputs = data['prompts']
fixed_prompt = f"You have to act as a {dom} assisting system and generate response to the last user utterance in the conversation:\n\n"


for i in range(len(inputs)):
    inputs[i] = f"{fixed_prompt}{inputs[i]}" 
    inputs[i] = f"<s> [INST] {inputs[i]} [/INST]"

        
outputs = llm.generate(inputs, sampling_params)


results = []
for i, output in enumerate(outputs):
    results.append(output.outputs[0].text)


dial_ids = data['diag_id']
conv_idxs = data['conv_idx']


with open(f'domain_res_gen_results/{dom}_mistral_with_venues.pickle', 'wb') as file:
    pickle.dump({"responses":results, "diag_id": dial_ids,"conv_idx": conv_idxs}, file)