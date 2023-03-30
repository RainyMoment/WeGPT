import openai
def chatgpt(question):
    openai.api_key = "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"

    prompt = "\nHuman: " + question
    
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt = question,
            temperature=0.9,
            max_tokens=2000,
            frequency_penalty=0,
            presence_penalty=0,
            stop=[" Human:"," AI:"]
        )
        
        result = response["choices"][0]["text"].strip()
        print(result)
        return result


    except Exception as exc:
        print(exc)

wechat = "1你又设置机器人"
if wechat[0] == "1":
   chatgpt(wechat)
