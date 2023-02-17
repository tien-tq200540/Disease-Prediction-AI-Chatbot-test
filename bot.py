from predict import predict_disease_from_symptom
from preprocess import word_extractor, symptoms

while True:
    print("Bot: Describe your symptoms!")
    description = input("You: ")
    final_symtoms = symptoms(word_extractor(description))
    print("Bot: You can be " + predict_disease_from_symptom(final_symtoms))