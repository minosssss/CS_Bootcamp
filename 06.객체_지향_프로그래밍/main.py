from function import *

if __name__ == "__main__":
    raw_data = get_data_from_excel('class_2_3.xlsx')
    scores = list(raw_data.values())

    avrg = average(scores)
    variance = variance(scores, avrg)
    standard_deviation = std_dev(variance)

    print(f"평균: {avrg}, 분산: {variance}, 표준편차: {standard_deviation}")

    #학년 전체 학생 평균: 50점
    evaluateClass(avrg, 50, standard_deviation, 20)