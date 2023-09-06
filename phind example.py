import re
import phind

# Define a function to return result to a prompt
def phind_ai(prompt):
  result = phind.Completion.create(
      model  = 'gpt-4',
      prompt = prompt,
      results     = phind.Search.create(prompt, actualSearch = False), # create search (set actualSearch to False to disable internet)
      creative    = False,
      detailed    = False,
      codeContext = '') # up to 3000 chars of code
  
  # Remove other stuff and formatting characters
  reply = str(result.completion.choices[0]).replace("""<__main__.APIResponse.Completion.Choices""", "").replace("""(
    text           = b'<PHIND_METADATA>{"model_name": "gpt-3.5"}</PHIND_METADATA>""", "").replace("""',
    index          = 0,
    logprobs       = None,
    finish_reason  = stop)object at 0x1337>""","").replace("\\r\\n\\r\\n","").replace("\\r\\n","").replace("\\","")

  # Use regex to remove square brackets and content inside it
  pattern = r'\[[^\]]*\]'
  reply = re.sub(pattern, '', reply)
  
  return reply

# Basic input and output cycle
print ("Enter prompt, get result")
print ("------------------------")
while True:
  reply = phind_ai(input(">>>>>> "))
  print ("Reply: ",reply)
