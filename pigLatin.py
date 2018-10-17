def pigLatin(statement):
	alpha = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
	vowel = "aeiouAEIOU"
	statementList = statement.split(" ")
	print(statementList)
	for i in range(len(statementList)):
		if statementList[i][0] not in alpha:
			statementList[i] = statementList[i][:] + " yay"
		else:
			if statementList[i][1] in alpha:
				statementList[i] = statementList[i][2:] + "-" + statementList[i][:2] + 'ay'
			else:
				statementList[i] = statementList[i][1:] + "-" + statementList[i][:1] + "ay"

	return " ".join(statementList)
