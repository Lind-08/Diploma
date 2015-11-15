def createFile(agentName, taskID, commandWithOptions={}):
    """
    The function creates script file with name "Agent_name_Task_number"
    and return this name.
    :param agentName: Agent name
    :param taskID: Task number
    :param commandWithOptions: Command with options and values for him
    :return:
    """
    fileName = agentName + "_" + taskID
    scriptFile = open(fileName, "w")
    scriptFile.write("#!/bin/bash\n")
    scriptFile.write(_createScriptString(commandWithOptions))
    scriptFile.close()
    return fileName

def _createScriptString(commandWithOptions={}):
    scriptString = ""
    if commandWithOptions:
        for elem in commandWithOptions:
            scriptString = scriptString + " " + commandWithOptions[elem]
    return scriptString
#TODO: Need adding verifying values for command's options

