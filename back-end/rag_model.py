from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

def generate_recommendations(location, job_title, salary, seniority_level):
    # Initialize the RAG tokenizer, retriever, and generation model
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base")
    retriever = RagRetriever.from_pretrained("facebook/rag-token-base")
    generator = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-base")

    # Generate recommendations using the RAG model
    prompt = f"Recommendations for {job_title} jobs in {location} with salary {salary} and seniority {seniority_level}."
    input_ids = tokenizer([prompt], return_tensors="pt").input_ids

    with retriever:
        retrieved_docs = retriever.retrieve(input_ids)[0]

    generated = generator.generate(input_ids=input_ids, context_input_ids=retrieved_docs)

    recommendations = tokenizer.batch_decode(generated, skip_special_tokens=True)

    return recommendations
