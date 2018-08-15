if __name__ == "__main__":

    with open("graph.json", "wt") as f:
        f.write("[\n")
        for i in range(2 ** 8 - 1):
            father = -1
            if (i % 2 == 0 and i > 0):
                father = (i - 2)/2
            elif (i % 2 != 0 and i > 0):
                father = (i - 1)/2
            if (father == -1):
                f.write("""  { "parent": \"\", "name": "%1d" },\n""" % i)
            else:
                f.write("""  { "parent": "%1d", "name": "%1d" },\n""" % (father, i))
        f.write("]")
