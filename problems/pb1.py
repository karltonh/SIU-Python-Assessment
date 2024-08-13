# declare and fill out function here


# test case
#sentence = "Test  This is a test   Testing "
#sentence2 = replace_spaces(sentence, "_")
#print(sentence2) # -> Test__This_is_a_test__Testing_

def replace_spaces(stringToReplace, replaceSpaceWith):
  newStr = stringToReplace.replace(' ',replaceSpaceWith)
  return newStr