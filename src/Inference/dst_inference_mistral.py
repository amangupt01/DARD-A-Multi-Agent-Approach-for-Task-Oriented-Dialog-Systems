import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm
import pickle

# Set the path to your model directory - TODO
model_path = "/path/to/your/model/directory"

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False, local_files_only=True)

# Load the model in a distributed manner
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto",
    local_files_only=True,
    pad_token_id=tokenizer.eos_token_id,
    max_memory={i: f"{torch.cuda.get_device_properties(i).total_memory * 0.8 / 1024**3:.2f}GiB" for i in range(torch.cuda.device_count())},
)

# Prepare input text
# input_text = """<INST>
# Track the dialogue states present in the following conversation:

# Now its your turn to answer, the following is the current conversation context:
# USER: I need to get to Cambridge by 10:15 for a business meeting, can you give me some train information.
# SYSTEM: I can help! Where are you departing from?
# USER: From Bishops Stortford on Tuesday.
# SYSTEM: Train TR0635 departs at 9:29 and arrives at 10:07. Would you like me to book you a ticket?
# USER: Not at this time, but could you give me the exact travel time please?


#  </INST>
# """

data = pickle.load(open('sav_text_prompts.pickle','rb'))

print(data.keys())

# inputs = [input_text]*20
inputs = data['prompts']

# import random
# random.shuffle(inputs)
# inputs = inputs[:30]

for i in range(len(inputs)):
    inputs[i] = f"Track the dialogue states present in the following conversation:\n\n{inputs[i]}" 
    inputs[i] = f"<s> [INST] {inputs[i]} [/INST]"

BATCH_SIZE = 32


results = []
dial_ids = []
conv_idxs = []

for i in tqdm(range(0, len(inputs), BATCH_SIZE)):
    batch = inputs[i:i+BATCH_SIZE]
    dial_ids.extend(data['diag_id'][i:i+BATCH_SIZE])
    conv_idxs.extend(data['conv_idx'][i:i+BATCH_SIZE])
    tokenized_inputs = tokenizer(batch, return_tensors="pt", padding=True, truncation=True).to("cuda")

    # Generate output
    with torch.no_grad():
        outputs = model.generate(**tokenized_inputs, max_new_tokens=1024)

    # Decode and store results
    generated_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    # for j, output in enumerate(outputs):
    #     generated_tokens = output[tokenized_inputs['input_ids'][j].size(0):]
    #     generated_text = tokenizer.decode(generated_tokens, skip_special_tokens=True)
    #     # print(generated_text)
    #     # print("X"*20)
    #     results.append(generated_text)

    results.extend(generated_text)

    if len(results)%(BATCH_SIZE*50) == 0:
        with open('generated_dst_generic_model_epoch10.pickle', 'wb') as file:
            pickle.dump({"responses":results, "diag_id": dial_ids,"conv_idx": conv_idxs}, file)

    # batch_results = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    # results.extend(batch_results)


with open('generated_dst_generic_model_epoch10.pickle', 'wb') as file:
    pickle.dump({"responses":results, "diag_id": dial_ids,"conv_idx": conv_idxs}, file)

