from sumado import mainfunction
from sumado.adjacency_lists import get_adj_list
import timeit
import json


def testing():
    def get_info_rel(reltype):
        rel = get_adj_list(reltype)
        nodes = get_number_nodes(rel)
        edges = get_number_edges(rel)
        return nodes, edges

    def get_number_nodes(rel):
        return len(rel)

    def get_number_edges(rel):
        return sum(len(j) for j in rel.values())

    def format_time(totaltime):
        totaltime *= 1000000
        totaltime = int(totaltime)
        return totaltime

    def time_calc(totaltime):
        totaltime = format_time(totaltime)
        diff = get_formated_diff(relativetime)
        return totaltime, diff

    def get_formated_diff(relativet):
        diff = relativet[-1] - relativet[0]
        if diff != 0:
            diff = (diff / relativet[0]) * 100
            diff = int(diff)
            diff = "+" + str(diff) + "%"
        else:
            diff = "-"
        return diff

    def print_head():
        nodes, edges = get_info_rel(typerel)
        print("\nTest for", i,
              "\n Number of Nodes:", nodes,
              "\n Number of Edges:", edges,
              "\n Total parts:", nodes + edges)

    def print_footer():
        print(" Time in microseconds: ", ttime,
              "\n Difference with first:", difference,
              "\n Pass = ", passed
              )

    def test(reltype):
        start_time = timeit.default_timer()
        output_raw = mainfunction.main(reltype, inputtest)
        time = timeit.default_timer() - start_time
        relativetime.append(time)
        time, diff = time_calc(time)
        output = json.loads(output_raw)
        return output, time, diff

    testcases = {
        "triangle": ([1, 2, 3, 4, 5, 6],
                     {
                         "vertexes": [1, 2, 3, 4, 5, 6],
                         "poligons": [7, 10, 11, 15]
                     }),
        "2x3": ([1, 2, 3, 4, 5, 6],
                {
                    "vertexes": [1, 2, 3, 4, 5, 6],
                    "poligons": [8, 10, 16]
                }),

        "3x3": ([8, 5, 9, 1, 7, 6, 2, 3, 4],
                {
                    "vertexes": [8, 5, 9, 1, 7, 6, 2, 3, 4],
                    "poligons": [20, 16, 27, 13, 17, 14]
                }),

        "4x4": ([7, 2, 6, 10, 8, 13, 1, 12, 15, 11, 3, 16, 5, 9, 4, 14],
                {
                    "vertexes": [7, 2, 6, 10, 8, 13, 1, 12, 15, 11, 3, 16, 5,
                                 9, 4, 140],
                    "poligons": [17, 22, 23, 28, 19, 47, 28, 32, 35, 29, 27,
                                 23, 34]
                }),

        "5x5": ([9, 1, 14, 23, 17, 16, 8, 18, 2, 25, 7, 22, 5, 20, 21, 11, 15,
                 6, 12, 13, 19, 4, 10, 3, 24],
                {
                    "vertexes": [9, 1, 14, 23, 17, 16, 8, 18, 2, 25, 7, 22, 5,
                                 20, 21, 11, 15, 6, 12, 13, 19, 4, 10, 3, 24],
                    "poligons": [34, 23, 39, 42, 67, 31, 52, 53, 45, 48, 55,
                                 33, 48, 43, 46, 49, 43, 29, 52, 25]
                })
    }
    print("Testing Main Function")

    relativetime = []
    passes = []

    totaltime = []

    for i in sorted(testcases):
        typerel = i[0]

        print_head()

        inputtest = testcases[i][0]
        result, ttime, difference = test(typerel)

        totaltime.append(ttime)

        expectedoutput = testcases[i][1]
        passed = result == expectedoutput
        passes.append(passed)

        print_footer()
    if all(passes):
        print("\n\n Totaltime:", sum(totaltime))
        print("Passed")
    else:
        print("Fail")

if __name__ == "__main__":
    testing()
