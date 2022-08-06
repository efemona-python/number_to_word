class GenerateWord:
    multiplier = ["", "thousand", "million", "billion", "trillion", "quadrillion","quintillion"]
    less_than_twenty = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                        9: "nine",
                        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    count = 1
    multiplier_count = 0



    def generate_words(self, number):
        number_in_words = []
        # print(number)
        global n_temp
        number_range = range(len(number))
        if int(number) < 20:
            number_in_words = self.less_than_twenty[int(number)]
        elif int(number) == 0:
            number_in_words = "zero"
        else:
            for i in number_range:
                n = number[::-1][i]

                #       check if units
                if self.count % 3 == 1:
                    #       check if the tens value is less than 20, hold n "unit" temporarily and add to tens value in next iteration
                    if i < len(number) - 1 and int(number[::-1][i + 1]) < 2:
                        n_temp = n
                    #             the number is less than 1000

                    else:
                        if self.multiplier_count < 1:
                            number_in_words.append(self.less_than_twenty[int(n)])
                        #             the unit of the multiplier is zero
                        elif int(n) == 0:
                            number_in_words.append(
                                self.less_than_twenty[int(n)] + self.multiplier[self.multiplier_count] + ", ")
                        #              the number is greater than 1000
                        else:
                            number_in_words.append(
                                self.less_than_twenty[int(n)] + " " + self.multiplier[self.multiplier_count] + ", ")

                #       check if tens
                elif self.count % 3 == 2:
                    #           if the tens value is less than 20
                    if int(n) < 2:
                        number_in_words.append(self.less_than_twenty[int(n + n_temp)])
                    else:
                        number_in_words.append(self.tens[int(n)] + "-")

                #       check if hundreds
                elif self.count % 3 == 0:
                    if int(n) == 0:
                        number_in_words.append("")
                    else:
                        number_in_words.append(self.less_than_twenty[int(n)] + " hundred and ")
                    #           the next value after HTU will be a multiplier
                    self.multiplier_count += 1

                self.count += 1
        return "".join(number_in_words[::-1]).capitalize().rstrip('-')
