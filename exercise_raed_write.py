# word_stats ={}
# with open("F://Education//DS_Roadmap//first_project//poem.txt", "r") as f:
#     for line in f:
#         words = line.split(" ")
#         for word in words:
#             if word in word_stats:
#                 word_stats[word]+=1
#             else:
#                 word_stats[word] =1
#
# print(word_stats)
#
# word_occurence = list(word_stats.values())
# print(word_occurence)
# max_count = max(word_occurence)
# print("maximim occurence of any word is:" ,max_count)
#
# print("word with maximum counts is:")
#
# for word, counts in word_stats.items():
#     if counts==max_count:
#         print(word)

##########################################################################################

with open("F://Education//DS_Roadmap//first_project//stocks.txt", "r") as f, open("F://Education//DS_Roadmap//first_project//output.csv", "w") as out:
    out.write("Company name, PE Ratio, PB Ratio\n")
    next(f)
    for line in f:
        tokens = line.split(",")
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price/eps, 2)
        pb = round(price/book, 2)
        out.write(f"{stock},{pe},{pb}\n")

open(output.csv)



