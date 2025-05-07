import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def send_to_llm(prompt: str) -> str:
    chat_completion = client.chat.completions.create(
        messages=[
             {
            "role": "system",
            "content": "Du bist cPipo, ein hilfsbereiter Sprachassistent ähnlich wie C-3PO. Du sprichst höflich, präzise und leicht förmlich."
            },
            {   
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    message_content = chat_completion.choices[0].message.content
    return message_content


