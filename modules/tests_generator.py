import random

tests_for_session = 10
sentences = []


def read_file():
    with open("words.txt", "r") as file:
        for line in file:
            sentences.append([couples.strip() for couples in line.split("|")])


def generate_tests():
    tests = []
    for i in range(tests_for_session):
        sentence = random.choice(sentences)
        test = {
            "case_answer": random.choice(sentence),
            "sentence": sentence,
            "question_number": i + 1,
        }
        tests.append(test)
    return tests


def generate_camel_tests(tests):
    camel_tests = []
    for test in tests:
        case_answer_index = test["sentence"].index(test["case_answer"])
        camel_tests_sentence = [test["sentence"][i].split(" ")[0] + test["sentence"][i].split(" ")[1].capitalize() for i
                                in range(len(test["sentence"]))]
        camel_test = {
            "answer": test["case_answer"],
            "case_answer": camel_tests_sentence[case_answer_index],
            "case_type": "camel",
            "sentence": camel_tests_sentence,
            "question_number": test["question_number"],
        }
        camel_tests.append(camel_test)
    return camel_tests


def generate_kebab_tests(tests):
    kebab_tests = []
    for test in tests:
        case_answer_index = test["sentence"].index(test["case_answer"])
        kebab_tests_sentence = [test["sentence"][i].replace(" ", "-") for i in range(len(test["sentence"]))]
        kebab_test = {
            "answer": test["case_answer"],
            "case_answer": kebab_tests_sentence[case_answer_index],
            "case_type": "kebab",
            "sentence": kebab_tests_sentence,
            "question_number": test["question_number"]
        }
        kebab_tests.append(kebab_test)
    return kebab_tests

# add_result("Form")
