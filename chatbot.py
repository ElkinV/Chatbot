import openai

openai.api_key="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"
conversation =""
i=1

while(i!=0):
    question = input("Humano: ")
    conversation += "\nHumano: "+ question +"\nAI:"
    response = openai.Completion.create(
        engine="davinci",
        prompt= conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", "Humamo:", "AI:"]
    )
    anwer = response.choices[0].text.strip()
    conversation+= anwer
    print("AI: "+ anwer+"\n")
    