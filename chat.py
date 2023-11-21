#from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from transformers import AutoTokenizer, AutoModel,AutoModelForCausalLM
from transformers.generation import GenerationConfig
from tqdm import tqdm
import json 
import os
import logging

# 参数设置
device = "auto"
model_path = "DUTIR-LegalIntelligence/tailing"
output_path = "<your_output_path>"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    low_cpu_mem_usage=True,
    torch_dtype=torch.float16,
    trust_remote_code=True,
    device_map = device
)

tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    trust_remote_code=True
)

logging.disable(logging.WARNING)
tokenizer.pad_token_id = tokenizer.eod_id
tokenizer.bos_token_id = tokenizer.eod_id
tokenizer.eos_token_id = tokenizer.eod_id

model.cuda()
model.eval()

def inference_dataset():
    # 加载数据
    data = input("inputs:")

    if os.path.exists(output_path):
        os.remove(output_path)
    
    if isinstance(data,str):
        res = chat(data)
        # 记录
        with open(output_path,"a") as file:
            json.dump(res,file,ensure_ascii=False)
            file.write("\n")
    elif isinstance(data,list):
        for sample in data:
            res = chat(sample)
            # 记录
            with open(output_path,"a") as file:
                json.dump(res,file,ensure_ascii=False)
                file.write("\n")


def chat(inputs:str):
    history_token_ids = torch.tensor([[]], dtype=torch.long)
    max_new_tokens = 1024
    top_p = 0.9
    top_k = 0
    temperature = 0.25
    repetition_penalty = 1.0

    history_max_len = 1000 
    #utterance_id = 0
    history_token_ids = None

    input_ids = tokenizer(inputs, return_tensors="pt", add_special_tokens=False).input_ids
    eos_token_id = torch.tensor([[tokenizer.eos_token_id]], dtype=torch.long)
    inputs_ids = torch.concat([input_ids, eos_token_id], dim=1)

    if history_token_ids is None:
        history_token_ids = inputs_ids
    else:
        history_token_ids = torch.cat((history_token_ids, inputs_ids), dim=1)

    # 开始对话
    model_input_ids = history_token_ids[:, -history_max_len:].to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            input_ids=model_input_ids, max_new_tokens=max_new_tokens, do_sample=True, top_p=top_p,top_k=top_k,
            temperature=temperature, repetition_penalty=repetition_penalty, eos_token_id=tokenizer.eos_token_id
        )
    model_input_ids_len = model_input_ids.size(1)
    response_ids = outputs[:, model_input_ids_len:]
    history_token_ids = torch.concat((history_token_ids, response_ids.cpu()), dim=1)
    response = tokenizer.batch_decode(response_ids)

    return response[0].strip().replace(tokenizer.eos_token, "")

if __name__ == "__main__":
    inference_dataset()
