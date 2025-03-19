from datasets import load_dataset
import json

# 1. Hugging Face 认证
HF_TOKEN = "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"

# 2. 加载 Hugging Face 数据集（显式传入 Token）
dataset_name = "VLM-Reasoner/deepscaler"
dataset = load_dataset(dataset_name, token=HF_TOKEN)

# 3. 保存为 JSONL
for split, data in dataset.items():
    output_file = f"{dataset_name.replace('/', '_')}_{split}.jsonl"
    
    with open(output_file, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    
    print(f"Saved {split} split to {output_file}")
