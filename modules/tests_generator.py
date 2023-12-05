import random

tests_for_session = 10
sentences = []


def read_file():
    with open("words.txt", "r") as file:
        for line in file:
            sentences.append([couples.strip() for couples in line.split("|")])


def generate_tests():
    tests = {}
    for i in range(tests_for_session):
        # sentence example:
        # [fast run, fasten rung, fast rug, fist run]
        case_type = random.choice(["kebab", "camel"])
        sentence = random.choice(sentences)
        for j in range(len(sentence)):
            if case_type == "kebab":
                sentence[j] = sentence[j].replace(" ", "-")
            else:
                sentence[j] = sentence[j].split(" ")[0] + sentence[j].split(" ")[1].capitalize()
        test = {
            "case_answer": random.choice(sentence),
            "case_type": case_type,
            "sentence": sentence
        }
        tests[i] = test
    return tests

# add_result("Form")