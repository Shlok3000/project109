import statistics
import csv
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
prep_list = df["test preparation course"].tolist()
math_list = df["math score"].tolist()
reading_list = df["reading score"].tolist()
writing_list = df["writing score"].tolist()

prep_mean = statistics.mean(prep_list)
math_mean = statistics.mean(math_list)
reading_mean = statistics.mean(reading_list)
writing_mean = statistics.mean(writing_list)

prep_mode = statistics.mode(prep_list)
math_mode = statistics.mode(math_list)
reading_mode = statistics.mode(reading_list)
writing_mode = statistics.mode(writing_list)

prep_median = statistics.median(prep_list)
math_median = statistics.median(math_list)
reading_median = statistics.median(reading_list)
writing_median = statistics.median(writing_list)

print("Mean, Median and Mode of height is {}, {} and {} respectively".format(prep_mean, prep_mode, prep_median))
print("Mean, Median and Mode of height is {}, {} and {} respectively".format(math_mean, math_mode, math_median))
print("Mean, Median and Mode of height is {}, {} and {} respectively".format(prep_mean, prep_mode, prep_median))
print("Mean, Median and Mode of height is {}, {} and {} respectively".format(reading_mean, reading_mode, reading_median))

prep_std_deviation = statistics.stdev(prep_list)
math_std_deviation = statistics.stdev(math_list)
reading_std_deviation = statistics.stdev(reading_list)
writing_std_deviation = statistics.stdev(writing_list)

prep_first_std_deviation_start, prep_first_std_deviation_end = prep_mean-prep_std_deviation, prep_mean+prep_std_deviation
prep_second_std_deviation_start, prep_second_std_deviation_end = prep_mean-(2*prep_std_deviation), prep_mean+(2*prep_std_deviation)
prep_third_std_deviation_start, prep_third_std_deviation_end = prep_mean-(3*prep_std_deviation), prep_mean+(3*prep_std_deviation)

math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)

reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)

writing_first_std_deviation_start, writing_first_std_deviation_end = writing_mean-reading_std_deviation, writing_mean+writing_std_deviation
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_mean-(2*writing_std_deviation), writing_mean+(2*writing_std_deviation)
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_mean-(3*writing_std_deviation), writing_mean+(3*writing_std_deviation)

prep_list_of_data_within_1_std_deviation = [result for result in prep_list if result > prep_first_std_deviation_start and result < prep_first_std_deviation_end]
prep_list_of_data_within_2_std_deviation = [result for result in prep_list if result > prep_second_std_deviation_start and result < prep_second_std_deviation_end]
prep_list_of_data_within_3_std_deviation = [result for result in prep_list if result > prep_third_std_deviation_start and result < prep_third_std_deviation_end]

math_list_of_data_within_1_std_deviation = [result for result in math_list if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in math_list if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in math_list if result > math_third_std_deviation_start and result < math_third_std_deviation_end]

reading_list_of_data_within_1_std_deviation = [result for result in reading_list if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_list_of_data_within_2_std_deviation = [result for result in reading_list if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_list_of_data_within_3_std_deviation = [result for result in reading_list if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]

writing_list_of_data_within_1_std_deviation = [result for result in writing_list if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_list_of_data_within_2_std_deviation = [result for result in writing_list if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_list_of_data_within_3_std_deviation = [result for result in writing_list if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]

print("{}% of data for prep tests lies within 1 standard deviation".format(len(prep_list_of_data_within_1_std_deviation)*100.0/len(prep_list)))
print("{}% of data for prep tests lies within 2 standard deviations".format(len(prep_list_of_data_within_2_std_deviation)*100.0/len(prep_list)))
print("{}% of data for prep tests lies within 3 standard deviations".format(len(prep_list_of_data_within_3_std_deviation)*100.0/len(prep_list)))

print("{}% of data for math tests lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_list)))
print("{}% of data for math tests lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(math_list)))
print("{}% of data for math tests lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(math_list)))

print("{}% of data for reading tests lies within 1 standard deviation".format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading tests lies within 2 standard deviations".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading tests lies within 3 standard deviations".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading_list)))

print("{}% of data for writing tests lies within 1 standard deviation".format(len(writing_list_of_data_within_1_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing tests lies within 2 standard deviations".format(len(writing_list_of_data_within_2_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing tests lies within 3 standard deviations".format(len(writing_list_of_data_within_3_std_deviation)*100.0/len(writing_list)))