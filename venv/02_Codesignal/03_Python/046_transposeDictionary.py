def transposeDictionary(scriptByExtension):
    return sorted([[v,k] for k, v in scriptByExtension.items()])

s = {
  "validate": "py",
  "getLimits": "md",
  "generateOutputs": "json"
}
print(transposeDictionary(s))