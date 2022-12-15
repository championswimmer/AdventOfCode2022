// cargo-deps: commons = { path = "../commons" }

fn main() {
    let lines = io::read_lines("day-01/input.txt");
    // create empty i32 vector
    let mut elf_calories: Vec<i32> = Vec::new();
    let mut curr_elf_calories = 0;
    // iterate through lines and add to vector
    for line in lines {
        if line == "" {
            elf_calories.push(curr_elf_calories);
            curr_elf_calories = 0;
        } else {
            curr_elf_calories += line.parse::<i32>().unwrap();
        }
    }
    // sort elfCalories in reverse order
    elf_calories.sort_by(|a, b| b.cmp(a));
    println!("{}", elf_calories[0] + elf_calories[1] + elf_calories[2])
    

}