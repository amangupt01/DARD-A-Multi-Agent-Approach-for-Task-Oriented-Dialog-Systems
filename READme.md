## DARD - Domain Assigned Response Delegation

This repository contains the code to reproduce the results quoted in the paper "DARD: A Multi-Agent Approach for Task-Oriented Dialog Systems"

We used the standardized evaluation established by [Nekvinda and Dusek,
2021](https://github.com/Tomiinek/MultiWOZ_Evaluation), we used an updated slot mapping which can be found in the file ```src/update_slot_mapping.py```. All the prediction files can be found in the ```data/predictions/``` folder

### Steps to reproduce the results

- Create a new conda environment using ```conda create -n myenv python=3.9``` and then install the required dependencies using ```pip install -r requirements.txt```.
- Clone the [MultiWOZ_Evaluation](https://github.com/Tomiinek/MultiWOZ_Evaluation) repository into the root directory. We use the MultiWOZ 2.2 dataset obtained using the instructions suggested on the READme of the MultiWOZ_Evaliation repository.
- Use the Claude Agent Prompts presented in the ```src/Claude_Agents``` directory to generate the Claude Agent predictions. You will need to use an external API call to query the model - "claude-3-5-sonnet-20240620"
- Use the training data provided in the folder ```data/training_data``` to fine-tune [Mistal-7B](https://huggingface.co/mistralai/Mistral-7B-v0.1) and [Flan-T5-large](https://huggingface.co/google/flan-t5-large). Note that we perform full-parameter fine-tuning(not parameter-efficient). Training time could vary depending on the kind of GPUs being used.
- The scripts provided in the folder ```src/Inference/``` can be used to generate the predictions from the fine-tuned model weights.
