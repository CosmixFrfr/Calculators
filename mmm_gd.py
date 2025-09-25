# Frequency
class_interval = []
frequency = []
mid_point = []
fxm = []
cumulative_frequency = []

def RoundOff(a):
    if (a * 1000) % 100 >= 5:
        return int(a * 100 + 0.5) / 100
    else:
        return int(a * 100) / 100

def input_val(prompt, datatype=str, errormessage="Invalid Value. Please try again."):
    while True:
        try:
            return datatype(input(prompt))
        except ValueError:
            print(errormessage)

def given_input(errormessage="Invalid Value. Please try again."):
    while True:
        lower = input_val("Lower class limit: ", int)
        upper = input_val("Upper class limit: ", int)

        lower_boundary = lower - 0.5
        upper_boundary = upper + 0.5
        class_interval.append((lower_boundary, upper_boundary))
        print(f"class interval: {class_interval}")

        freq = input_val("Frequency: ", int)
        frequency.append(freq)
        print(f"frequency: {frequency}")
        
        if_continue = input_val("Continue? (Y for yes): ")
        if if_continue.upper() != "Y":
            break

    total_cf = 0
    for i in range(len(frequency)):
        midpoint = (class_interval[i][0] + class_interval[i][1]) / 2
        mid_point.append(midpoint)

        fxm.append(frequency[i] * midpoint)

        total_cf += frequency[i]
        cumulative_frequency.append(total_cf)

    print("\nFrequency Distribution Table")
    print("Class Interval   |  f  |   m   |  f*m   | C.F.")
    print("------------------------------------------------")
    for i in range(len(class_interval)):
        ci = f"{class_interval[i][0]}-{class_interval[i][1]}"
        print(f"{ci:<15} | {frequency[i]:<3} | {mid_point[i]:<5} | {fxm[i]:<6} | {cumulative_frequency[i]:<3}")

    print("------------------------------------------------")
    print(f"Total f   = {sum(frequency)}")
    print(f"Total f*m = {sum(fxm)}")

    mmm_response = input_val("Mean, Median, Mode? (Y/N): ")
    if mmm_response.upper() == "Y":
        # mean
        mean = RoundOff(sum(fxm) / sum(frequency))
        
        # median
        N = sum(frequency)
        N2 = N / 2
        for i, cf in enumerate(cumulative_frequency):
            if cf >= N2:
                median_class = i
                break
        L = class_interval[median_class][0]
        f = frequency[median_class]
        median_cf = cumulative_frequency[median_class - 1] if median_class > 0 else 0
        i_size = class_interval[median_class][1] - class_interval[median_class][0]
        median = RoundOff(L + ((N2 - median_cf) / f) * i_size)
        
        # mode
        modal_class = frequency.index(max(frequency))
        Lm = class_interval[modal_class][0]
        f1 = frequency[modal_class]
        f0 = frequency[modal_class - 1] if modal_class > 0 else 0
        f2 = frequency[modal_class + 1] if modal_class < len(frequency) - 1 else 0
        i_size_mode = class_interval[modal_class][1] - class_interval[modal_class][0]
        mode = RoundOff(Lm + ((f1 - f0) / (2 * f1 - f0 - f2)) * i_size_mode if (2 * f1 - f0 - f2) != 0 else None)

        print("------------------------------------------------")
        print(f"Mean   = {mean}")
        print(f"Median = {median}")
        if mode is not None:
            print(f"Mode   = {mode}")
        else:
            print("Mode   = Undefined (division by zero)")
        print("Program Success!")
    else:
        return

given_input()
