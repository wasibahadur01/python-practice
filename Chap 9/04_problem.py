def generate_tables(n):
    tables = ""
    for i in range(1, 11):
        tables += f"{n} * {i} = {n * i}\n"

    with open (f"tables/table_{n}.txt", "w") as file:
        file.write(tables)



for i in range(2,21):
    generate_tables(i)