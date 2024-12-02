use std::fs::read_to_string;

fn check_vector(input: Vec<&str>) -> bool {
        let mut deltas : Vec<i32> = Vec::new();
        let mut signs : Vec<bool> = Vec::new();

        for i in 1..input.len(){
            let cur: i32 = input[i].parse().expect("Not a number");
            let prev:i32 = input[i-1].parse().expect("Not a number");

            deltas.push( ( cur-prev).abs() );
            signs.push( ( cur-prev) >= 0 );
        }

        // Check the level differences
        let a = signs.iter().fold(true, |res,x| res & x);
        let b = signs.iter().fold(true, |res,x| res & !x);

        let sign = a|b;

        let cor = *deltas.iter().max().unwrap() < 4 && *deltas.iter().min().unwrap() > 0 && sign;

        return cor;
}

fn main() {
    let filename = "input.txt";
    let mut part1 : i32 = 0;
    let mut part2 : i32 = 0;

    for line in read_to_string(filename).unwrap().lines() {
        let s: Vec<&str> = line.split_whitespace().collect();

        // Initial one
        let fnord = s.clone();
        let cor = check_vector(fnord);
        if cor {
            part1 +=1;
            continue;
        }

        // We start dropping stuff..
        // Probably sub-optimzal, but meh..
        for i in 0..s.len() {
            let mut tmp = s.clone();
            tmp.remove(i);
            let correct = check_vector(tmp);

            if correct {
                part2 +=1;
                break;
            }
        }
    }

    let total_p2 = part1 + part2;

    println!("Part 0: {part1}");
    println!("Part 2: {total_p2}");
}
