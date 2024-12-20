use regex::Regex;
use std::fs::read_to_string;

/**
* Notes: A bit fugly implementation, but could not be
* bothered to generalize it..
*/

static mut mul_enable: bool = false;

fn count_occ2(string: &str) -> i32 {
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)").unwrap();

    let mut total : i32 = 0;

    for cap in re.captures_iter(string) {

        unsafe {
            if &cap[0] == "do()" {
                mul_enable = true;
                continue;
            } else if &cap[0] == "don't()" {
                mul_enable = false;
                continue;
            }
        }

        // Otherwise we are in a MUL(x,y) section
        let ci0 : i32 = cap[1].parse().expect("Failed to parse string");
        let ci1 : i32 = cap[2].parse().expect("Failed to parse string");

        unsafe {
            if mul_enable {
                total +=  ci0 * ci1;
            }
        }
    }
    return total;
}

fn count_occ(string: &str) -> i32 {
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();

    let mut total : i32 = 0;

    for cap in re.captures_iter(string) {
        let ci0 : i32 = cap[1].parse().expect("Failed to parse string");
        let ci1 : i32 = cap[2].parse().expect("Failed to parse string");

        total +=  ci0 * ci1;
    }
    return total;
}

fn main() {
    let filename = "input.txt";

    unsafe {
        mul_enable = true;
    };

    let mut total : i32 = 0;

    for line in read_to_string(filename).unwrap().lines() {
        total += count_occ(&line);
    }

    println!("Part 1: {}", total);

    total = 0;
    for line in read_to_string(filename).unwrap().lines() {
        total += count_occ2(&line);
    }

    println!("Part 2: {}", total);

}
