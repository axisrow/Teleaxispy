import gradio as gr

def greet(name):
    return "Hello " + name + "!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0", port=8080, debug=True, share=False)
