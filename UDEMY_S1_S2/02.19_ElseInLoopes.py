instruction = ["say hi", "say hallo", "abort", "move arm"]
instructionApproved =[]

for instr in instruction:
    print("Adding instruction : ",instr)
    instructionApproved.append(instr)

    if instr == "abort":
         print("Aborting")
         instructionApproved.clear()
         break

else:
    print("Folowing instructions will be taken : ", instructionApproved)




