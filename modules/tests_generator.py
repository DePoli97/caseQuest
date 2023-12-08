import random

tests_for_session = 10
sentences = []


def read_file():
    with open("words.txt", "r") as file:
        for line in file:
            sentences.append([words.strip() for words in line.split("|")])


def generate_tests():
    tests = []
    for i in range(tests_for_session):
        sentence = random.choice(sentences)
        test = {
            "case_answer": random.randint(0, len(sentence) - 1),
            "sentence": sentence,
            "question_number": i + 1,
        }
        tests.append(test)
    return tests


def generate_type_tests(tests, type):
    type_tests = []
    for test in tests:
        type_tests_sentence = []
        for couple in test["sentence"]:
            words = couple.split(" ")
            text = words[0]
            for i in range(1, len(words)):
                text += words[i].capitalize() if type == "camel" else '-' + words[i]
            type_tests_sentence.append(text)

        type_test = {
            "answer": test['sentence'][test['case_answer']],
            "case_answer": type_tests_sentence.index(type_tests_sentence[test['case_answer']]),
            "case_type": type,
            "sentence": type_tests_sentence,
            "question_number": test["question_number"],
        }
        print(type_test)
        type_tests.append(type_test)
    return type_tests

