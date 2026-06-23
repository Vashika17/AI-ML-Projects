from retriever import retrieve
from generator import generate_answer

query = input("Ask something: ")
context = retrieve(query)
answer = generate_answer(context, query)

print(answer)
