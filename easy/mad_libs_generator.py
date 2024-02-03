"""Mad libs generator."""

# pylint: disable=E0401
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

MODEL_NAME = "gpt2"

model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
tokenizer = GPT2Tokenizer.from_pretrained(MODEL_NAME)

user_input = input("Enter prompt: ")
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

story = generator(user_input, max_length=100)

print(f"Story: {story[0]['generated_text']}")
