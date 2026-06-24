try:
    n1 = int(input("Enter number of students in group 1:"))
    group1 = {}
    for i in range(n1):
        text = input("enter student (cod, name):  ")
        parts = text.split(", ")
        code = int(parts[0])
        name = parts[1]
        group1[code] = name

    n2 = int(input("Enter number of students in group 2:"))
    group2 = {}
    for i in range(n2):
        text = input("enter student (cod, name):  ")
        parts = text.split(", ")
        code = int(parts[0])
        name = parts[1]
        group2[code] = name

    common = {}
    for code in group1:
        if code in group2:
            if group1[code] == group2[code]:
                common[code] = group1[code]

    if len(common) == 0:
        print("No common students found.")
    else:
        codes = list(common.keys())
        codes.sort()
        print("Common students (sorted by code):")
        for code in codes:
            print(code, "-", common[code])

except ValueError:
    print("Error enter valid num")
except IndexError:
    print("code, name  (must have space after comma)")
except Exception as e:
    print(f"unexpected error {e}")