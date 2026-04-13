letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "John").replace("<|Date|>", "2024-06-30"))