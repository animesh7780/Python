from openai import OpenAI

client = OpenAI(
    api_key = "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"
)

response = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": "Say this is a test",
    }],
    model="gpt-4o-mini",
)

print(response._request_id)