from transformers import AutoTokenizer, AutoModelForCausalLM

# Basic LLM code from huggingface starter
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it")

# model.config(hidden_activation="hidden_act")

input_text = "What is 1 + 1? Only answer with the answer."
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(
    **input_ids,
    max_new_tokens=50
    )

print(tokenizer.decode(outputs[0]))
