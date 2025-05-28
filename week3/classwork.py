#

# Answer after splitting and conversion to a float.
try:
    str = "X-DSPAM-Confidence: 0.8475"

    # Find the colon in the string above.
    newStr = str.find(":")
    # print(newStr)

    word = str[newStr + 1:]
    # Splitted Word
    print(word)


except:
    print("Not a float Number")

ans = float(word)
print(f"\nThe result is {ans} in {type(ans)} format.")
# print(type(ans))



# Teacher's Solution



try:
    sent = "X-DSPAM-Confidence: 8475"

    newSent = sent.split()
    if len(newSent) != 2:
        exit()

    if newSent[0] != "X-DSPAM-Confidence:":
        exit()

    #print(newSent)
    answer = float(newSent[1])

    print(answer)
    print(type(answer))

    #print(f"The output is %.5f of {type(answer)}.\n" %answer)
except:
    print("Not a float Number.")

#print(answer)
