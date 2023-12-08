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
            "case_answer": random.choice(sentence),
            "sentence": sentence,
            "question_number": i + 1,
        }
        tests.append(test)
    return tests


def generate_type_tests(tests, type):
    camel_tests = []
    for test in tests:
        camel_tests_sentence = []
        for couple in test["sentence"]:
            words = couple.split(" ")
            text = words[0]
            for i in range(1, len(words)):
                text += words[i].capitalize() if type == "camel" else '-' + words[i]
            camel_tests_sentence.append(text)

        camel_test = {
            "answer": test["case_answer"],
            "case_answer": test['case_answer'],
            "case_type": "camel",
            "sentence": camel_tests_sentence,
            "question_number": test["question_number"],
        }
        camel_tests.append(camel_test)
    return camel_tests
