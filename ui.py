import gradio as gr
import os
import oxen
from oxen.auth import config_auth
from oxen.user import config_user
import json
import jsonlines

#FILL THESE IN WITH YOUR API KEY, NAME AND EMAIL
# config_auth("YOUR_AUTH_TOKEN")
# config_user("YOUR NAME", "YOUR EMAIL")
# config_auth("SFMyNTY.g2gDbQAAAC9hcGlfa2V5X3YxOjZhMzc3ZDgwLWIzNDktNGJiMy05MTRjLTJlMWRiYzcyMzExOW4GAAUD01ONAWIAAVGA.er2ApA3y4ruimvCR71C2Wm5ixUbidTeaHAoxYa6X8gc")
# config_user("Nick Chu", "nyc8pv@gmail.com")



bad_prompt = ""

# Function to update the bad_prompt variable
def update_bad_prompt(input_text):
    '''
    saves prompt to prompts.json
    '''
    global bad_prompt
    bad_prompt = input_text
    #save bad_prompt as json 

    file_path = "prompts.jsonl"
    data = [{"Prompt": bad_prompt}]
    with jsonlines.open(file_path, 'a') as writer:
        writer.write_all(data)
    return bad_prompt

def oxbutton_callback():
    '''
    when button is clicked, prompts.json is pushed to oxen repo, clear jsonl
    '''
    return "button clicked"


with gr.Blocks() as demo:
    gr.Markdown("Type the ChatGPT bad prompt in the textbox below. Click Submit to save it to json on disk. Click Save to Oxen to save the prompts to Oxen.")
    prompt = gr.Textbox(label = "Enter bad prompt here", lines = 2)
    button1 = gr.Button(value = "Save prompt to json")
    button1.click(update_bad_prompt, inputs = prompt)

    #save the jsonl to oxen repo
    oxbutton = gr.Button(value="Save to Oxen")
    oxbutton.click(oxbutton_callback)

# demo = gr.Interface(
#     fn=update_bad_prompt,
#     inputs=gr.Textbox(label = "Enter the bad ChatGPT Prompt here"),
#     outputs=["text"]
# )


demo.launch()
demo.close()