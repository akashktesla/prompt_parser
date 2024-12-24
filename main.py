#universal prompt parser
import re

def parse_prompt(path,var_config = {}):
  messages = []
  #read the data
  with open(path,"r") as f:
    file_data = f.read()
  # print(f'Data: { file_data }')
  #remove comments
  pattern_comments = r"#.+"
  file_data = re.sub(pattern_comments,"",file_data)

  pattern_variable = "({.+?})"
  matches = re.finditer(pattern_variable,file_data)
  for match in matches:
    variable = match.group(1)
    var2 = variable.replace("{","")
    var2 = var2.replace("}","")
    print(f"variable: {variable}")
    file_data = file_data.replace(variable,var_config[var2])
    print(f"file_data: {file_data}")

  pattern_tag = r"<(\w+)>(.+?)</\1>"  # Updated to make the inner content non-greedy
  matches = re.finditer(pattern_tag, file_data)
  for match in matches:
      role = match.group(1)        # Captures the tag name
      content = match.group(2)    # Captures the content inside the tag
      messages.append({"role":role,"content":content})
  return messages

def main():
  var_config = {"user_query":"testing1234"}
  messages = parse_prompt("t2g.prompt",var_config)
  print(f"Messages: { messages }") 

if __name__ == "__main__":
  main()
