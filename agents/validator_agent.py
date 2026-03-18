from openai import OpenAI

client = OpenAI()

def validate_sow(extracted_text):

    prompt = f"""
You are a contract validator.

Analyze the following SOW document text and identify:

1. Missing fields
2. Contract risks
3. Invalid clauses
4. Compliance issues

SOW Content:
{extracted_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content